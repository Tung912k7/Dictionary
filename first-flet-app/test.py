
import openpyxl
import flet as ft

def main(page: ft.Page):
    # Load the Excel file (replace with your actual file path)
    wb = openpyxl.load_workbook("data.xlsx")
    sheet = wb.active # Get the active sheet

    # Define a dictionary to store search results (key: search term, value: list of matching rows)
    search_results = {}

    def handle_search(e):
        search_term = e.control.value.lower() # Ensure case-insensitive search

        if search_term:
            # Clear previous search results
            search_results.clear()

            # Iterate through rows, starting from row 2 (assuming headers in row 1)
            for row in sheet.iter_rows(min_row=3):
                # Check if any cell value in the row contains the search term (case-insensitive)
                if any(str(cell.value).lower().find(search_term) != -1 for cell in row):
                    search_results[search_term] = search_results.get(search_term, []) + [list(row)] # Append matching rows

            # Update the results container
            results_container.controls.clear()
            if search_results:
                for result in search_results[search_term]:
                    results_container.controls.append(
                        ft.Text(
                            ", ".join([str(cell.value) for cell in result]),
                            no_wrap=False
                        )
                    )
                results_container.update()
            else:
                results_container.controls.append(ft.Text("No results found."))
                results_container.update()
        else:
            # Clear results if search bar is empty
            search_results.clear()
            results_container.controls.clear()
            results_container.update()

    # Search bar
    search_bar = ft.SearchBar(
        on_change=handle_search,
        bar_hint_text="Search Excel data...",
        view_bgcolor = '#E6E6FA'
    )

    # Container to display search results
    results_container = ft.Column(controls=[])

    # Corrected Row structure to make results_container flexible within the row:
    search_row = ft.Column(wrap = True,
        controls=[search_bar, results_container], # Use controls instead of children
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )


    page.add(search_row)

ft.app(target=main)
