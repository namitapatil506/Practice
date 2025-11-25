from playwright.sync_api import Page, expect
def test_page_has_get_started_link(page:Page):
    page.goto("http://uitestingplayground.com/dynamictable")
    label=page.locator("p.bg-warning").inner_text()
    percentage=label.split()[-1]

    column_headers= page.get_by_role("columnheader")

    cpu_column=None
    for index in range(column_headers.count()):
        column_header=column_headers.nth(index)

        if column_header.inner_text=="Network":
            print(column_header)
            cpu_column= index
            print(cpu_column)
            break

    assert cpu_column != None

    #located rows-->2 row grp --> and selected 2nd/last
    rowgroup = page.get_by_role("rowgroup").last

    #to find chrome row grp
    chrome_row = rowgroup.get_by_role("row").filter(has_text="Chrome")

    chrome_cpu = chrome_row.get_by_role("cell").nth(cpu_column)

    expect(chrome_cpu).to_have_text(percentage)



    
    