import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter import Canvas
import pandas as pd
from datetime import datetime
import os
import json

class K9TrainingApp:
    def __init__(self, root):
        self.root = root
<<<<<<< HEAD
        self.root.title("K-9 QUICK Version 1.3 BETA")
=======
        self.root.title("K-9 QUICK Version 1.2")
>>>>>>> main
        self.root.geometry("1250x1000")
        self.training_aids_list = []
        self.view_tree = None

        # Data file path
        self.data_file = "k9_records.csv"

        # Create scrollable canvas
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.canvas = Canvas(self.main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar_y = ttk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_x = ttk.Scrollbar(self.root, orient=tk.HORIZONTAL, command=self.canvas.xview)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.canvas.configure(yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.content_frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.content_frame, anchor="nw")

        # Creating input fields
        self.create_widgets()

<<<<<<< HEAD
        self.enable_mouse_wheel_scrolling()

        # Load existing data
        self.load_data()
        
    def enable_mouse_wheel_scrolling(self):
        # Bind for Windows / Linux
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

=======
        # Load existing data
        self.load_data()
>>>>>>> main

    def create_widgets(self):
        button_frame = tk.Frame(self.content_frame, padx=10, pady=10)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        self.save_button = tk.Button(button_frame, text="Save Record", command=self.save_record)
        self.save_button.pack(side="left", padx=5)

        self.load_button = tk.Button(button_frame, text="Load CSV", command=self.load_csv)
        self.load_button.pack(side="left", padx=5)

        self.view_button = tk.Button(button_frame, text="View Records", command=self.open_view_window)
        self.view_button.pack(side="left", padx=5)

<<<<<<< HEAD
        self.update_button = tk.Button(button_frame, text="Update Record", command=self.update_record, state='disabled')
=======
        self.update_button = tk.Button(button_frame, text="Update Record", command=self.update_record)
>>>>>>> main
        self.update_button.pack(side="left", padx=5)

        self.new_button = tk.Button(button_frame, text="New Record", command=self.new_record)
        self.new_button.pack(side="left", padx=5)

<<<<<<< HEAD
        self.merge_button = tk.Button(button_frame, text="Merge", command=self.merge_csv)
        self.merge_button.pack(side="left", padx=5)

        # -------------------------
        # MAIN INPUT FRAME (row=1)
        # -------------------------
=======
>>>>>>> main
        input_frame = tk.Frame(self.content_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        input_frame.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

        tk.Label(input_frame, text="K-9 Name").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.k9_name_entry = tk.Entry(input_frame, width=30)
        self.k9_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Handler's Name").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.handler_name_entry = tk.Entry(input_frame, width=30)
        self.handler_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Date (YYYY-MM-DD)").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.date_entry = tk.Entry(input_frame, width=30)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))

        tk.Label(input_frame, text="Time Start (HH:MM)").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.time_start_entry = tk.Entry(input_frame, width=30)
        self.time_start_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Time Stop (HH:MM)").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.time_stop_entry = tk.Entry(input_frame, width=30)
        self.time_stop_entry.grid(row=4, column=1, padx=10, pady=5)

<<<<<<< HEAD
        # -------------------------
        # TRAINING SECTION (row=2)
        # -------------------------
        tk.Label(self.content_frame, text="TRAINING", font=("Helvetica", 14, "bold")).grid(
            row=2, column=0, padx=10, pady=10, sticky='n')

        # ----------------------------------------
        # TRAINING AID FRAME (row=3, column=0)
        # ----------------------------------------
=======
        # Training Section
        tk.Label(self.content_frame, text="TRAINING", font=("Helvetica", 14, "bold")).grid(
            row=2, column=0, padx=10, pady=10, sticky='n')

>>>>>>> main
        training_aid_frame = tk.Frame(self.content_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        training_aid_frame.grid(row=3, column=0, padx=10, pady=5, sticky='nsew')

        tk.Label(training_aid_frame, text="Training Aid Type").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.training_aid_type_entry = tk.Entry(training_aid_frame, width=30)
        self.training_aid_type_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(training_aid_frame, text="Training Aid Weight").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.training_aid_weight_entry = tk.Entry(training_aid_frame, width=30)
        self.training_aid_weight_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(training_aid_frame, text="Set Time").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.set_time_entry = tk.Entry(training_aid_frame, width=30)
        self.set_time_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(training_aid_frame, text="Search Start Time").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.search_start_time_entry = tk.Entry(training_aid_frame, width=30)
        self.search_start_time_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(training_aid_frame, text="Search Stop Time").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.search_stop_time_entry = tk.Entry(training_aid_frame, width=30)
        self.search_stop_time_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(training_aid_frame, text="Hide Location & Details").grid(row=5, column=0, padx=10, pady=5, sticky='w')
        self.hide_location_entry = tk.Entry(training_aid_frame, width=30)
        self.hide_location_entry.grid(row=5, column=1, padx=10, pady=5)

        # Checkboxes for Alert Types
        tk.Label(training_aid_frame, text="Alert Types").grid(row=6, column=0, padx=10, pady=5, sticky='w')
        self.alert_types_vars = {
            "Positive Alert": tk.BooleanVar(),
            "Handler Assisted": tk.BooleanVar(),
            "Change in Behavior": tk.BooleanVar(),
            "Negative Alert": tk.BooleanVar()
        }

<<<<<<< HEAD
        row = 7
=======
        row = 7  # Starting row for the checkboxes
>>>>>>> main
        for alert_type, var in self.alert_types_vars.items():
            checkbox = tk.Checkbutton(training_aid_frame, text=alert_type, variable=var)
            checkbox.grid(row=row, column=0, padx=10, pady=2, sticky='w')
            row += 1

<<<<<<< HEAD
        # Button to add/save training aids
        self.add_aid_button = tk.Button(training_aid_frame, text="Save Aid / Add Another Aid", command=self.add_training_aid)
        self.add_aid_button.grid(row=row, column=1, sticky='e', padx=10, pady=5)

        # ------------------------------------------------------------
        # (Moved) FRAME FOR ADDED TRAINING AIDS --> now inside the same
        # 'training_aid_frame' instead of row=3, col=1 in content_frame
        # ------------------------------------------------------------
        self.aid_list_frame = tk.Frame(training_aid_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        self.aid_list_frame.grid(row=row+1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')
=======
        # Save Aid Button
        self.add_aid_button = tk.Button(training_aid_frame, text="Save Aid / Add Another Aid", command=self.add_training_aid)
        self.add_aid_button.grid(row=row, column=1, sticky='e', padx=10, pady=5)

        # ------------------------------------------------
        # 4. FRAME FOR ADDED TRAINING AIDS (row=3, col=1)
        # ------------------------------------------------
        self.aid_list_frame = tk.Frame(self.content_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        self.aid_list_frame.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')
>>>>>>> main

        tk.Label(self.aid_list_frame, text="Added Training Aids").pack(anchor='w')

        self.aid_list_scrollbar = tk.Scrollbar(self.aid_list_frame)
        self.aid_list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.aid_list_text = tk.Text(self.aid_list_frame, width=50, height=12,
                                    wrap='word',
                                    yscrollcommand=self.aid_list_scrollbar.set)
        self.aid_list_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
<<<<<<< HEAD
        self.aid_list_scrollbar.config(command=self.aid_list_text.yview)
        self.aid_list_text.bind("<Double-1>", self.edit_training_aid)

        # ------------------------------------------------------------
        # NEW FRAME WHERE THE OLD "ADDED TRAINING AIDS" FRAME WAS:
        # row=3, column=1 in the content_frame
        # ------------------------------------------------------------
        self.training_checkbox_frame = tk.Frame(self.content_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        self.training_checkbox_frame.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

        # Add label or heading for this new frame
        tk.Label(self.training_checkbox_frame, text="Training Options", font=("Helvetica", 12, "bold")).pack(anchor='w', pady=5)

        # Create BooleanVars for each checkbox
        self.obedience_var = tk.BooleanVar()
        self.bite_work_var = tk.BooleanVar()
        self.article_search_var = tk.BooleanVar()
        self.gun_fire_var = tk.BooleanVar()
        self.muzzle_var = tk.BooleanVar()
        self.building_search_var = tk.BooleanVar()

        tk.Checkbutton(self.training_checkbox_frame, text="Obedience", variable=self.obedience_var).pack(anchor='w')
        tk.Checkbutton(self.training_checkbox_frame, text="Bite Work", variable=self.bite_work_var).pack(anchor='w')
        tk.Checkbutton(self.training_checkbox_frame, text="Article Search", variable=self.article_search_var).pack(anchor='w')
        tk.Checkbutton(self.training_checkbox_frame, text="Gun Fire", variable=self.gun_fire_var).pack(anchor='w')
        tk.Checkbutton(self.training_checkbox_frame, text="Muzzle", variable=self.muzzle_var).pack(anchor='w')
        tk.Checkbutton(self.training_checkbox_frame, text="Building Search", variable=self.building_search_var).pack(anchor='w')

        tk.Label(self.training_checkbox_frame, text="Miscellaneous:").pack(anchor='w', pady=(10, 0))
        self.misc_entry = tk.Entry(self.training_checkbox_frame, width=30)
        self.misc_entry.pack(anchor='w', padx=5, pady=5)

        # ------------------------------------------------
        # DEPLOYMENT (row=4)
=======

        self.aid_list_scrollbar.config(command=self.aid_list_text.yview)
        
        self.aid_list_text.bind("<Double-1>", self.edit_training_aid)

        # ------------------------------------------------
        # 5. CASE DETAILS FRAME (row=4)
>>>>>>> main
        # ------------------------------------------------
        tk.Label(self.content_frame, text="DEPLOYMENT", font=("Helvetica", 14, "bold")).grid(
            row=4, column=0, padx=10, pady=10, sticky='n')

        case_details_frame = tk.Frame(self.content_frame, borderwidth=2, relief="groove", padx=10, pady=10)
        case_details_frame.grid(row=5, column=0, padx=10, pady=5, sticky='nsew')

        tk.Label(case_details_frame, text="Case Number").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.case_number_entry = tk.Entry(case_details_frame, width=30)
        self.case_number_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(case_details_frame, text="Vehicle Description/Registration").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.vehicle_description_entry = tk.Entry(case_details_frame, width=30)
        self.vehicle_description_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(case_details_frame, text="Suspect Name").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.suspect_name_entry = tk.Entry(case_details_frame, width=30)
        self.suspect_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(case_details_frame, text="Date of Birth/License Number").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.dob_license_entry = tk.Entry(case_details_frame, width=30)
        self.dob_license_entry.grid(row=3, column=1, padx=10, pady=5)

        # ------------------------------------------------
<<<<<<< HEAD
        # NARRATIVE (row=6)
        # ------------------------------------------------
        tk.Label(self.content_frame, text="Narrative").grid(row=6, column=0, padx=10, pady=5, sticky='nw')
        self.narrative_text = tk.Text(self.content_frame, width=80, height=10)
        self.narrative_text.grid(row=7, column=0, padx=10, pady=5, sticky='w')    
=======
        # 6. NARRATIVE (row=6)
        # ------------------------------------------------
        tk.Label(self.content_frame, text="Narrative").grid(row=6, column=0, padx=10, pady=5, sticky='nw')
        self.narrative_text = tk.Text(self.content_frame, width=80, height=10)
        self.narrative_text.grid(row=7, column=0, padx=10, pady=5, sticky='w')
        
>>>>>>> main

    def add_training_aid(self):
        #Add a new training aid or update an existing one."""
        # Gather input data
        aid_data = {
            "Training Aid Type": self.training_aid_type_entry.get(),
            "Training Aid Weight": self.training_aid_weight_entry.get(),
            "Set Time": self.set_time_entry.get(),
            "Search Start Time": self.search_start_time_entry.get(),
            "Search Stop Time": self.search_stop_time_entry.get(),
            "Hide Location & Details": self.hide_location_entry.get(),
            "Alert Types": [alert for alert, var in self.alert_types_vars.items() if var.get()]
        }

        # If editing an existing aid, update it
        if hasattr(self, "editing_aid_index") and self.editing_aid_index is not None:
            self.training_aids_list[self.editing_aid_index] = aid_data
            del self.editing_aid_index  # Clear editing state
        else:
            # Otherwise, add it as a new aid
            self.training_aids_list.append(aid_data)
              # Clear fields and refresh the aid list display
            self.training_aid_type_entry.delete(0, tk.END)
            self.training_aid_weight_entry.delete(0, tk.END)
            self.set_time_entry.delete(0, tk.END)
            self.search_start_time_entry.delete(0, tk.END)
            self.search_stop_time_entry.delete(0, tk.END)
            self.hide_location_entry.delete(0, tk.END)

            for var in self.alert_types_vars.values():
                var.set(False)

            self.refresh_aid_list_display()
            
    def refresh_aid_list_display(self):
        #Refresh the display of training aids in the aid list text widget.
        self.aid_list_text.delete("1.0", tk.END)  # Clear the widget content

        # Populate the widget with training aids
        for idx, aid_data in enumerate(self.training_aids_list, start=1):
            display_str = (
                f"{idx}. "
                f"Type: {aid_data.get('Training Aid Type', 'N/A')}, "
                f"Weight: {aid_data.get('Training Aid Weight', 'N/A')}, "
                f"Set: {aid_data.get('Set Time', 'N/A')}, "
                f"Start: {aid_data.get('Search Start Time', 'N/A')}, "
                f"Stop: {aid_data.get('Search Stop Time', 'N/A')}, "
                f"Location: {aid_data.get('Hide Location & Details', 'N/A')}, "
                f"Alerts: {', '.join(aid_data.get('Alert Types', []))}\n"
            )
            self.aid_list_text.insert(tk.END, display_str)

        # Ensure text color is visible
        self.aid_list_text.configure(fg="black", bg="white")  # Adjust colors if needed



    def save_record(self):
        #Save the entire record (including multiple training aids) to CSV.
        # Serialize all training aids as JSON and store under one column
        training_aids_json = json.dumps(self.training_aids_list)

        record = {
            "K-9 Name": self.k9_name_entry.get(),
            "Handler Name": self.handler_name_entry.get(),
            "Date": self.date_entry.get(),
            "Time Start": self.time_start_entry.get(),
            "Time Stop": self.time_stop_entry.get(),
            # Single column to hold all multiple aids:
            "Training Aids": training_aids_json,
            "Case Number": self.case_number_entry.get(),
            "Vehicle Description/Registration": self.vehicle_description_entry.get(),
            "Suspect Name": self.suspect_name_entry.get(),
            "Date of Birth/License Number": self.dob_license_entry.get(),
            "Narrative": self.narrative_text.get("1.0", tk.END).strip()
        }

        # Replace empty inputs with a single space (existing logic)
        record = {key: value if value.strip() else " " for key, value in record.items()}

        try:
            # Convert the record into a DataFrame and append it to the CSV
            file_exists = os.path.exists(self.data_file)
            df = pd.DataFrame([record])
            df.to_csv(self.data_file, mode='a', index=False, header=not file_exists)
            messagebox.showinfo("Success", "Record saved successfully.")

            # Clear out the training_aids_list after saving, if desired
            self.training_aids_list.clear()
            self.aid_list_text.delete("1.0", tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Error saving record: {e}")


    def load_data(self):
        pass

    def load_csv(self):
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            self.data_file = file
            self.load_data()

    def open_view_window(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View and Sort Records")
        view_window.geometry("1000x600")

        tk.Label(view_window, text="Sort/Filter By").pack(pady=10)
        self.sort_by_combo = ttk.Combobox(view_window, values=[
            "K-9 Name", "Handler Name", "Date", "Case Number", "Vehicle Description/Registration"
        ])
        self.sort_by_combo.pack(pady=5)

        tk.Label(view_window, text="Enter Value to Filter").pack(pady=10)
        self.filter_entry = tk.Entry(view_window)
        self.filter_entry.pack(pady=5)

        filter_button = tk.Button(view_window, text="Apply Filter/Sort", command=self.apply_filter_sort)
        filter_button.pack(pady=10)

        columns = [
            "K-9 Name", "Handler Name", "Date", "Time Start", "Time Stop",
            "Training Aids",                # Single JSON column for all aids
            "Case Number", "Vehicle Description/Registration",
            "Suspect Name", "Date of Birth/License Number", "Narrative"
        ]

        self.view_tree = ttk.Treeview(view_window, columns=columns, show="headings")
        for col in columns:
            self.view_tree.heading(col, text=col)
            self.view_tree.column(col, width=150)
        self.view_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.view_tree.bind("<Double-1>", self.populate_main_form_from_view)

        self.load_view_data()

    def populate_main_form_from_view(self, event):
        #Populate the main form when a record is double-clicked in the View Records window.
        selected_item = self.view_tree.selection()
        if selected_item:
            record_values = self.view_tree.item(selected_item, "values")
            field_names = [
                "K-9 Name", "Handler Name", "Date", "Time Start", "Time Stop",
                "Training Aids",  # single JSON-based column
                "Case Number", "Vehicle Description/Registration",
                "Suspect Name", "Date of Birth/License Number", "Narrative"
            ]

            # Clear old aids and the aid list text widget
            self.aid_list_text.delete("1.0", tk.END)
            self.training_aids_list.clear()

            for i, field_name in enumerate(field_names):
                value = record_values[i] if i < len(record_values) else ""

                if field_name == "Training Aids":
                    # Parse the JSON-based training aids
                    try:
                        self.training_aids_list = json.loads(value) if value else []
                    except json.JSONDecodeError:
                        self.training_aids_list = []

                    # Refresh the display of training aids
                    self.refresh_aid_list_display()

                elif field_name == "Narrative":
                    self.narrative_text.delete("1.0", tk.END)
                    self.narrative_text.insert("1.0", value)

                else:
                    # For other fields, populate their respective input widgets
                    entry_attr = field_name.lower().replace(" ", "_") + "_entry"
                    if hasattr(self, entry_attr):
                        entry_widget = getattr(self, entry_attr)
                        entry_widget.delete(0, tk.END)
                        entry_widget.insert(0, value)

            # Enable the Update Record button
            self.update_button.config(state='normal')

            
    def edit_training_aid(self, event):
    #Handle double-click on a training aid to populate fields for editing."""
        try:
            # Get the index of the selected line
            index = self.aid_list_text.index(f"@{event.x},{event.y}").split(".")[0]
            index = int(index) - 1  # Convert to zero-based index
            
            if 0 <= index < len(self.training_aids_list):  # Ensure valid index
                # Retrieve the selected training aid data
                selected_aid = self.training_aids_list[index]

                # Populate the input fields with the aid's data
                self.training_aid_type_entry.delete(0, tk.END)
                self.training_aid_type_entry.insert(0, selected_aid.get("Training Aid Type", ""))

                self.training_aid_weight_entry.delete(0, tk.END)
                self.training_aid_weight_entry.insert(0, selected_aid.get("Training Aid Weight", ""))

                self.set_time_entry.delete(0, tk.END)
                self.set_time_entry.insert(0, selected_aid.get("Set Time", ""))

                self.search_start_time_entry.delete(0, tk.END)
                self.search_start_time_entry.insert(0, selected_aid.get("Search Start Time", ""))

                self.search_stop_time_entry.delete(0, tk.END)
                self.search_stop_time_entry.insert(0, selected_aid.get("Search Stop Time", ""))

                self.hide_location_entry.delete(0, tk.END)
                self.hide_location_entry.insert(0, selected_aid.get("Hide Location & Details", ""))

                # Set checkbox states based on the selected aid's Alert Types
                for alert, var in self.alert_types_vars.items():
                    var.set(alert in selected_aid.get("Alert Types", []))

                # Store the index of the currently editing aid
                self.editing_aid_index = index
            else:
                messagebox.showwarning("Invalid Selection", "Please select a valid training aid.")
        except Exception as e:
            messagebox.showerror("Error", f"Error editing training aid: {e}")


    def apply_filter_sort(self):
        if not os.path.exists(self.data_file):
            messagebox.showerror("Error", "No data file found.")
            return
        try:
            df = pd.read_csv(self.data_file)
            sort_by = self.sort_by_combo.get()
            filter_value = self.filter_entry.get()
            if sort_by:
                df = df.sort_values(by=sort_by)
            if filter_value:
                df = df[df[sort_by].astype(str).str.contains(filter_value, case=False, na=False)]
            self.view_tree.delete(*self.view_tree.get_children())
            for _, row in df.iterrows():
                self.view_tree.insert("", "end", values=row.tolist())
        except Exception as e:
            messagebox.showerror("Error", f"Error applying filter/sort: {e}")

    def load_view_data(self):
        if os.path.exists(self.data_file):
            try:
                df = pd.read_csv(self.data_file)
                self.view_tree.delete(*self.view_tree.get_children())
                for _, row in df.iterrows():
                    self.view_tree.insert("", "end", values=row.tolist())
            except Exception as e:
                messagebox.showerror("Error", f"Error loading records: {e}")
                
    def new_record(self):
        """Clear all input fields, text widgets, training aids, and reset checkboxes."""
        # Clear main form entries
        self.k9_name_entry.delete(0, tk.END)
        self.handler_name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.date_entry.insert(0, datetime.now().strftime("%Y-%m-%d"))  # Set default date
        self.time_start_entry.delete(0, tk.END)
        self.time_stop_entry.delete(0, tk.END)
        self.case_number_entry.delete(0, tk.END)
        self.vehicle_description_entry.delete(0, tk.END)
        self.suspect_name_entry.delete(0, tk.END)
        self.dob_license_entry.delete(0, tk.END)
        self.narrative_text.delete("1.0", tk.END)

        # Clear training aid fields
        self.training_aid_type_entry.delete(0, tk.END)
        self.training_aid_weight_entry.delete(0, tk.END)
        self.set_time_entry.delete(0, tk.END)
        self.search_start_time_entry.delete(0, tk.END)
        self.search_stop_time_entry.delete(0, tk.END)
        self.hide_location_entry.delete(0, tk.END)

        # Reset alert type checkboxes
        for var in self.alert_types_vars.values():
            var.set(False)

        # Disable update button
        self.update_button.config(state='disabled')

        # Show confirmation message
        messagebox.showinfo("New Record", "All fields have been cleared.")

<<<<<<< HEAD
    def merge_csv(self):
            file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if not file:
                return

            try:
                # Read existing file
                existing_df = pd.read_csv(self.data_file) if os.path.exists(self.data_file) else pd.DataFrame()
                # Read new file
                new_df = pd.read_csv(file)

                # Merge data
                if not existing_df.empty:
                    merged_df = pd.concat([existing_df, new_df]).drop_duplicates(keep='first')
                else:
                    merged_df = new_df

                # Save merged data back to the original file
                merged_df.to_csv(self.data_file, index=False)
                messagebox.showinfo("Success", "Files merged successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error merging files: {e}")


=======
>>>>>>> main
                    
    def update_record(self):
        if self.view_tree is None:
            messagebox.showwarning("Warning", "You must open the View Records window before updating a record.")
            return
    
        # Otherwise, continue with accessing self.view_tree
        selected_item = self.view_tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "No record selected for update.")
            return
   
        try:
            # Re-serialize the training aids as JSON
            training_aids_json = json.dumps(self.training_aids_list)
            # Collect updated values from the main form
            updated_record = {
            "K-9 Name": self.k9_name_entry.get(),
            "Handler Name": self.handler_name_entry.get(),
            "Date": self.date_entry.get(),
            "Time Start": self.time_start_entry.get(),
            "Time Stop": self.time_stop_entry.get(),
            "Training Aids": training_aids_json,  # Store multiple aids in one column
            "Case Number": self.case_number_entry.get(),
            "Vehicle Description/Registration": self.vehicle_description_entry.get(),
            "Suspect Name": self.suspect_name_entry.get(),
            "Date of Birth/License Number": self.dob_license_entry.get(),
            "Narrative": self.narrative_text.get("1.0", tk.END).strip()
        }

            # Load existing data
            if not os.path.exists(self.data_file):
                messagebox.showerror("Error", "No data file found to update records.")
                return

            df = pd.read_csv(self.data_file)

            # Get the selected record from the Treeview
            selected_item = self.view_tree.selection()
            if selected_item:
                # Get the index of the selected record in the DataFrame
                record_index = int(self.view_tree.index(selected_item[0]))

                # Update the DataFrame with the new values
                for field, value in updated_record.items():
                    if field in df.columns:
                        df.at[record_index, field] = value

                # Save the updated DataFrame back to the CSV file
                df.to_csv(self.data_file, index=False)
                messagebox.showinfo("Success", "Record updated successfully.")
                
                # Refresh the view and disable the update button
                self.load_view_data()
                self.update_button.config(state='disabled')
            else:
                messagebox.showerror("Error", "No record selected for update.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update record: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = K9TrainingApp(root)
    root.mainloop()
