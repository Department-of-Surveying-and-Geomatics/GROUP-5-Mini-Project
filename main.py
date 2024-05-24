import tkinter as tk
from tkinter import filedialog
from data_parsing import dataParsing
from traverse_analysis import analyze_traverse_data
from Plotting import plot_traverse

class TraverseAnalyzerGUI:
    """GUI for the Traverse Analyzer application."""

    def __init__(self, master):
        self.master = master
        master.title("Traverse Analyzer")

        # Create GUI elements
        self.file_label = tk.Label(master, text="Traverse Data File:")
        self.file_label.pack()

        self.file_entry = tk.Entry(master)
        self.file_entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.point1_label = tk.Label(master, text="Point 1:")
        self.point1_label.pack()

        self.point1_entry = tk.Entry(master)
        self.point1_entry.pack()

        self.point2_label = tk.Label(master, text="Point 2:")
        self.point2_label.pack()

        self.point2_entry = tk.Entry(master)
        self.point2_entry.pack()

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze)
        self.analyze_button.pack()

        self.result_text = tk.Text(master, height=10, width=50)
        self.result_text.pack()

    def browse_file(self):
        """Open a file dialog and populate the file entry field with the selected file path."""
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)

    def analyze(self):
        """Perform the traverse analysis and display the results."""
        file_path = self.file_entry.get()
        point1 = int(self.point1_entry.get())
        point2 = int(self.point2_entry.get())

        try:
            traverse_df = dataParsing(file_path)
            analysis_results = analyze_traverse_data(traverse_df, point1, point2)
            plot_traverse(traverse_df, analysis_results, point1, point2, self.master)
            self.display_results(analysis_results, point1, point2)
        except FileNotFoundError:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, "Error: File not found.")
        except (ValueError, TypeError) as e:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Error: {e}")
        except Exception as e:
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"Unexpected error: {e}")

    def display_results(self, analysis_results, point1, point2):
        """Display the analysis results in the GUI."""
        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, f"Total number of traverse points (legs): {analysis_results['num_legs'] - 1}\n")
        self.result_text.insert(tk.END, f"Minimum Easting: {analysis_results['min_easting']}\n")
        self.result_text.insert(tk.END, f"Maximum Easting: {analysis_results['max_easting']}\n")
        self.result_text.insert(tk.END, f"Minimum Northing: {analysis_results['min_northing']}\n")
        self.result_text.insert(tk.END, f"Maximum Northing: {analysis_results['max_northing']}\n")
        self.result_text.insert(tk.END, f"Distance between points {point1} and {point2}: {analysis_results['distance']} meters\n")
        self.result_text.insert(tk.END, f"Bearing between points {point1} and {point2}: {analysis_results['bearing_degrees']}° {analysis_results['bearing_minutes']}' {analysis_results['bearing_seconds']}\" \n")

def main():
    """Main entry point for the Traverse Analyzer application."""
    root = tk.Tk()
    app = TraverseAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
