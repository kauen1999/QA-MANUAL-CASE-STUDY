import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright


# FIXTURE PRINCIPAL — cria o browser e a page
@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Aguarda preparo inicial do Playwright
        page.wait_for_load_state("domcontentloaded")
        
        yield page
        browser.close()



# HOOK PARA SCREENSHOT EM CASO DE FALHA
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            screenshots_dir = "reports/html/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_path = f"{screenshots_dir}/{item.name}_{timestamp}.png"

            page.screenshot(path=screenshot_path)

            if hasattr(report, "extra"):
                from pytest_html.extras import image
                report.extra.append(image(screenshot_path))


# TÍTULO DO RELATÓRIO
def pytest_html_report_title(report):
    report.title = "Relatório de Testes Automatizados"


# METADADOS (FORMA NOVA)
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend(["Projeto: Automação SauceDemo"])
    prefix.extend(["Autor: Jocean"])
