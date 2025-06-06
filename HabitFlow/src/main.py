import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QLabel, QTabWidget,
                             QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QAction,
                             QSpacerItem, QSizePolicy, QPushButton, QFrame, QProgressBar,
                             QLineEdit, QListWidget, QSlider, QTimeEdit, QSpinBox,
                             QCheckBox, QTextEdit)
from PyQt5.QtCore import Qt # Qt is already here, ensure it's used for Qt.Horizontal
from PyQt5.QtGui import QFont

class HabitFlowApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("HabitFlow")
        self.setGeometry(100, 100, 800, 600)  # x, y, width, height

        # Top Toolbar
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        # Logo Placeholder
        logo_label = QLabel("HabitFlow")
        logo_label.setStyleSheet("font-size: 20px; font-weight: bold; margin-left: 10px;")
        toolbar.addWidget(logo_label)

        # Spacer to push actions to the right
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        toolbar.addWidget(spacer)

        # Toolbar Actions (Settings, User)
        settings_action = QAction("Settings", self)
        user_action = QAction("User", self)
        toolbar.addAction(settings_action)
        toolbar.addAction(user_action)

        # Tab Widget for Main Content
        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        # Tabs
        daily_tracking_tab = QWidget()
        score_statistics_tab = QWidget()
        goal_setting_tab = QWidget()

        tab_widget.addTab(daily_tracking_tab, "Daily Tracking")
        tab_widget.addTab(score_statistics_tab, "Score Statistics")
        tab_widget.addTab(goal_setting_tab, "Goal Setting")

        # Example content for tabs (optional, can be expanded later)
        # --- Daily Tracking Tab ---
        daily_tracking_tab_layout = QHBoxLayout(daily_tracking_tab)

        # Left Panel (25%)
        left_panel_frame = QFrame()
        left_panel_frame.setFrameShape(QFrame.StyledPanel) # Add border for visualization
        left_panel_layout = QVBoxLayout(left_panel_frame)
        left_panel_layout.setAlignment(Qt.AlignTop) # Ensure alignment is top

        # Date Selector Container
        date_selector_widget = QWidget()
        date_selector_layout = QHBoxLayout(date_selector_widget)
        date_selector_layout.setContentsMargins(0,0,0,0) # Remove margins for tighter packing

        # Date Selector Components
        prev_date_button = QPushButton("<")
        current_date_label = QLabel("Today")
        current_date_label.setAlignment(Qt.AlignCenter)
        next_date_button = QPushButton(">")

        date_selector_layout.addWidget(prev_date_button)
        date_selector_layout.addWidget(current_date_label, 1) # Label takes available space
        date_selector_layout.addWidget(next_date_button)

        left_panel_layout.addWidget(date_selector_widget) # Added to left_panel_layout

        # "Habit Categories" Title Label
        habit_categories_title_label = QLabel("Habit Categories")
        habit_categories_title_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        left_panel_layout.addWidget(habit_categories_title_label)

        # Habit Categories Container
        habit_categories_container = QWidget()
        habit_categories_layout = QVBoxLayout(habit_categories_container)
        habit_categories_layout.setContentsMargins(0, 0, 0, 0) # Optional: remove margins

        default_categories = ["Health & Fitness", "Productivity", "Learning", "Mindfulness"]
        for category_name in default_categories:
            category_item_widget = QWidget()
            category_item_layout = QVBoxLayout(category_item_widget)
            # No margins for tighter packing of label and progress bar
            category_item_layout.setContentsMargins(5, 2, 5, 2)

            category_label = QLabel(f"{category_name}: 0%")
            progress_bar = QProgressBar()
            progress_bar.setValue(0)
            progress_bar.setFixedHeight(15) # Adjust height for better look

            category_item_layout.addWidget(category_label)
            category_item_layout.addWidget(progress_bar)

            habit_categories_layout.addWidget(category_item_widget)

        left_panel_layout.addWidget(habit_categories_container)

        # Daily Progress Summary Section
        # Completion Rate Label
        completion_rate_label = QLabel("0%")
        rate_font = QFont()
        rate_font.setPointSize(30)
        rate_font.setBold(True)
        completion_rate_label.setFont(rate_font)
        completion_rate_label.setAlignment(Qt.AlignCenter)
        left_panel_layout.addWidget(completion_rate_label)

        # Descriptive Text Label
        descriptive_text_label = QLabel("You've completed 0 out of 10 habits today!")
        descriptive_text_label.setAlignment(Qt.AlignCenter)
        left_panel_layout.addWidget(descriptive_text_label)

        # Inspirational Quote Label
        inspirational_quote_label = QLabel("Keep going! Every step counts.")
        inspirational_quote_label.setAlignment(Qt.AlignCenter)
        left_panel_layout.addWidget(inspirational_quote_label)

        left_panel_layout.addStretch(1) # Push all content to top

        # Right Panel (75%)
        right_panel_frame = QFrame()
        right_panel_frame.setFrameShape(QFrame.StyledPanel) # Add border for visualization
        right_panel_layout = QVBoxLayout(right_panel_frame) # This is the main layout for the right panel

        # Time Grid Container
        time_grid_container = QWidget()
        time_grid_layout = QGridLayout(time_grid_container)
        time_grid_layout.setSpacing(2) # Small spacing for a tighter grid

        # Empty top-left corner
        time_grid_layout.addWidget(QLabel(""), 0, 0)

        # Day Axis (Horizontal)
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for col, day in enumerate(days):
            day_label = QLabel(day)
            day_label.setAlignment(Qt.AlignCenter)
            time_grid_layout.addWidget(day_label, 0, col + 1)

        # Time Axis (Vertical)
        for hour in range(24):
            time_label_str = f"{hour:02d}:00"
            time_label = QLabel(time_label_str)
            time_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter) # Align text to the right
            time_grid_layout.addWidget(time_label, hour + 1, 0)

        # Placeholder for the main grid area
        grid_placeholder_label = QLabel("Time slots will appear here")
        grid_placeholder_label.setAlignment(Qt.AlignCenter)
        # Span from row 1, col 1, over 24 rows and 7 columns
        time_grid_layout.addWidget(grid_placeholder_label, 1, 1, 24, 7)


        right_panel_layout.addWidget(time_grid_container)
        # right_panel_layout.addStretch() # Remove stretch if grid should fill space, or keep if other elements are planned

        daily_tracking_tab_layout.addWidget(left_panel_frame, 1) # 25% stretch factor
        daily_tracking_tab_layout.addWidget(right_panel_frame, 3) # 75% stretch factor

        # --- Score Statistics Tab ---
        score_statistics_main_layout = QVBoxLayout(score_statistics_tab) # Main layout for the tab
        score_statistics_tab.setLayout(score_statistics_main_layout) # Explicitly set layout for the tab widget

        # Upper Score Area (35% height)
        upper_score_area_frame = QFrame()
        upper_score_area_frame.setFrameShape(QFrame.StyledPanel) # For visualization
        upper_score_area_layout = QHBoxLayout(upper_score_area_frame)

        # Left Section (Today's Score)
        today_score_section = QFrame()
        today_score_layout = QVBoxLayout(today_score_section)
        today_score_label = QLabel("0")
        today_score_font = QFont()
        today_score_font.setPointSize(50)
        today_score_font.setBold(True)
        today_score_label.setFont(today_score_font)
        today_score_label.setAlignment(Qt.AlignCenter)
        today_score_layout.addWidget(today_score_label)
        upper_score_area_layout.addWidget(today_score_section, 1) # Equal stretch, takes 1/3rd

        # Center Section (Score Composition)
        score_composition_section = QFrame()
        score_composition_layout = QVBoxLayout(score_composition_section)
        score_composition_label = QLabel("Score Composition (Details will appear here)")
        score_composition_label.setAlignment(Qt.AlignCenter)
        score_composition_layout.addWidget(score_composition_label)
        upper_score_area_layout.addWidget(score_composition_section, 1) # Equal stretch

        # Right Section (Quick Stats)
        quick_stats_section = QFrame()
        quick_stats_layout = QVBoxLayout(quick_stats_section)
        quick_stats_label = QLabel("Quick Stats (vs Yesterday, Weekly Avg will be here)")
        quick_stats_label.setAlignment(Qt.AlignCenter)
        quick_stats_layout.addWidget(quick_stats_label)
        upper_score_area_layout.addWidget(quick_stats_section, 1) # Equal stretch

        # Lower Charts Area (65% height)
        lower_charts_area_frame = QFrame()
        lower_charts_area_frame.setFrameShape(QFrame.StyledPanel) # For visualization
        # Set QHBoxLayout for the lower_charts_area_frame
        lower_charts_main_layout = QHBoxLayout(lower_charts_area_frame)

        # Left Chart Section
        left_chart_section = QFrame()
        # left_chart_section.setFrameShape(QFrame.Box) # For visualization
        left_chart_layout = QVBoxLayout(left_chart_section) # To center content
        trend_line_label = QLabel("Trend Line Chart (Weekly/Monthly)")
        trend_line_label.setAlignment(Qt.AlignCenter)
        left_chart_layout.addWidget(trend_line_label)
        lower_charts_main_layout.addWidget(left_chart_section, 1) # Equal stretch

        # Center Chart Section
        center_chart_section = QFrame()
        # center_chart_section.setFrameShape(QFrame.Box) # For visualization
        center_chart_layout = QVBoxLayout(center_chart_section) # To center content
        radar_chart_label = QLabel("Habit Completion Rate Radar Chart")
        radar_chart_label.setAlignment(Qt.AlignCenter)
        center_chart_layout.addWidget(radar_chart_label)
        lower_charts_main_layout.addWidget(center_chart_section, 1) # Equal stretch

        # Right Chart Section
        right_chart_section = QFrame()
        # right_chart_section.setFrameShape(QFrame.Box) # For visualization
        right_chart_layout = QVBoxLayout(right_chart_section) # To center content
        heatmap_label = QLabel("Yearly Heatmap")
        heatmap_label.setAlignment(Qt.AlignCenter)
        right_chart_layout.addWidget(heatmap_label)
        lower_charts_main_layout.addWidget(right_chart_section, 1) # Equal stretch

        # Add frames to the main tab layout with stretch factors
        score_statistics_main_layout.addWidget(upper_score_area_frame, 35) # 35% stretch factor
        score_statistics_main_layout.addWidget(lower_charts_area_frame, 65) # 65% stretch factor

        # --- Goal Setting Tab ---
        goal_setting_main_layout = QHBoxLayout(goal_setting_tab) # Main layout for the tab
        goal_setting_tab.setLayout(goal_setting_main_layout)

        # Left Habit List Panel (30% width)
        left_habit_list_panel = QFrame()
        left_habit_list_panel.setFrameShape(QFrame.StyledPanel) # For visualization
        left_habit_list_layout = QVBoxLayout(left_habit_list_panel)

        search_habits_input = QLineEdit()
        search_habits_input.setPlaceholderText("Search Habits")
        left_habit_list_layout.addWidget(search_habits_input)

        habit_list_widget = QListWidget()
        # Add some dummy items to habit_list_widget for visualization during development (optional)
        # for i in range(5):
        #     habit_list_widget.addItem(f"Sample Habit {i+1}")
        left_habit_list_layout.addWidget(habit_list_widget, 1) # QListWidget takes most space

        add_custom_habit_button = QPushButton("Add New Custom Habit")
        left_habit_list_layout.addWidget(add_custom_habit_button)

        goal_setting_main_layout.addWidget(left_habit_list_panel, 3) # 30% stretch factor

        # Right Habit Settings Panel (70% width)
        right_habit_settings_panel = QFrame()
        right_habit_settings_panel.setFrameShape(QFrame.StyledPanel) # For visualization
        right_habit_settings_layout = QVBoxLayout(right_habit_settings_panel)
        # Removed placeholder: settings_placeholder_label = QLabel("Selected Habit Settings Will Appear Here")

        # Habit Name
        right_habit_settings_layout.addWidget(QLabel("Habit Name:"))
        habit_name_input = QLineEdit()
        right_habit_settings_layout.addWidget(habit_name_input)

        # Habit Icon
        right_habit_settings_layout.addWidget(QLabel("Habit Icon:"))
        icon_placeholder_label = QLabel("Icon Placeholder") # Actual icon later
        right_habit_settings_layout.addWidget(icon_placeholder_label)

        # Goal Frequency
        right_habit_settings_layout.addWidget(QLabel("Goal Frequency (days per week):"))
        frequency_slider = QSlider(Qt.Horizontal)
        frequency_slider.setRange(1, 7)
        frequency_slider.setValue(1)
        # You might want to add a QLabel to display the slider's current value
        right_habit_settings_layout.addWidget(frequency_slider)

        # Goal Time Period
        right_habit_settings_layout.addWidget(QLabel("Goal Start Time:"))
        goal_start_time_edit = QTimeEdit()
        right_habit_settings_layout.addWidget(goal_start_time_edit)
        right_habit_settings_layout.addWidget(QLabel("Goal End Time:"))
        goal_end_time_edit = QTimeEdit()
        right_habit_settings_layout.addWidget(goal_end_time_edit)

        # Goal Duration
        right_habit_settings_layout.addWidget(QLabel("Minimum Duration (minutes):"))
        duration_spinbox = QSpinBox()
        duration_spinbox.setRange(0, 360) # e.g., 0 to 6 hours
        right_habit_settings_layout.addWidget(duration_spinbox)

        # Reminder Settings
        enable_reminder_checkbox = QCheckBox("Enable Reminder")
        right_habit_settings_layout.addWidget(enable_reminder_checkbox)
        right_habit_settings_layout.addWidget(QLabel("Reminder Time:")) # Visibility based on checkbox later
        reminder_time_edit = QTimeEdit()
        right_habit_settings_layout.addWidget(reminder_time_edit)

        # Notes
        right_habit_settings_layout.addWidget(QLabel("Notes:"))
        notes_text_edit = QTextEdit()
        notes_text_edit.setPlaceholderText("Enter any notes for this habit...")
        notes_text_edit.setFixedHeight(100) # Example fixed height
        right_habit_settings_layout.addWidget(notes_text_edit)

        # Action Buttons
        buttons_layout = QHBoxLayout()
        save_goal_button = QPushButton("Save Goal")
        reset_settings_button = QPushButton("Reset Settings")
        buttons_layout.addWidget(save_goal_button)
        buttons_layout.addWidget(reset_settings_button)
        buttons_layout.addStretch(1) # Push buttons to left
        right_habit_settings_layout.addLayout(buttons_layout)

        right_habit_settings_layout.addStretch(1) # Push all elements to the top

        goal_setting_main_layout.addWidget(right_habit_settings_panel, 7) # 70% stretch factor

        # Floating Action Button (FAB) for Quick Record
        self.fab_quick_record = QPushButton("+", self) # Parent is self (QMainWindow)
        self.fab_quick_record.setFixedSize(60, 60)
        self.fab_quick_record.setStyleSheet(
            "QPushButton {"
            "  background-color: orange;"
            "  color: white;"
            "  border-radius: 30px;" # half of fixed size for circular shape
            "  font-size: 24px;" # Adjusted for better "+" visibility
            "  font-weight: bold;"
            "}"
            "QPushButton:hover {"
            "  background-color: #ffc966;" # Lighter orange on hover
            "}"
        )
        self.fab_quick_record.setCursor(Qt.PointingHandCursor)

        # Quick Record Panel
        self.quick_record_panel = QFrame(self) # Parent is self (QMainWindow)
        self.quick_record_panel.setFrameShape(QFrame.StyledPanel)
        self.quick_record_panel.setFixedSize(250, 180) # Adjusted size
        self.quick_record_panel.setStyleSheet(
            "QFrame {"
            "  background-color: #f0f0f0;" # Light gray
            "  border: 1px solid #cccccc;"
            "  border-radius: 5px;"
            "}"
        )
        # Layout for the panel's content
        panel_layout = QVBoxLayout(self.quick_record_panel)
        panel_label = QLabel("Quick Record Panel Content")
        panel_label.setAlignment(Qt.AlignCenter)
        panel_layout.addWidget(panel_label)
        # Add more placeholders later as needed
        # panel_layout.addWidget(QLabel("Common habit shortcuts..."))
        # panel_layout.addWidget(QPushButton("Record current activity"))

        self.quick_record_panel.hide() # Initially hidden

        # Connect FAB click to toggle panel
        self.fab_quick_record.clicked.connect(self.toggle_quick_record_panel)

        # Initial positioning (will be updated by resizeEvent)
        self.fab_quick_record.move(self.width() - 70, self.height() - 70)
        self.quick_record_panel.move(self.width() - 260, self.height() - 260)

        # Initialize database
        print("Attempting to initialize database...")
        try:
            from .database import create_tables, add_default_habit_categories
            print("Database module imported. Calling create_tables()...")
            create_tables()
            print("create_tables() called. Calling add_default_habit_categories()...")
            add_default_habit_categories()
            print("add_default_habit_categories() called. Database initialization process completed.")
        except ImportError as e:
            print(f"MAIM_PY: Error importing database module: {e}")
        except Exception as e: # Catch other potential errors during DB init
            print(f"MAIN_PY: Error during database initialization: {e}")

        self.show()

    def toggle_quick_record_panel(self):
        if self.quick_record_panel.isVisible():
            self.quick_record_panel.hide()
        else:
            # Ensure panel is raised to top when shown
            self.quick_record_panel.raise_()
            self.quick_record_panel.show()
            # Position it correctly (resizeEvent also handles this, but good for immediate show)
            self.position_quick_record_elements()


    def position_quick_record_elements(self):
        # Position FAB
        fab_x = self.width() - self.fab_quick_record.width() - 20 # 20px margin
        fab_y = self.height() - self.fab_quick_record.height() - 20
        self.fab_quick_record.move(fab_x, fab_y)

        # Position Panel (above and slightly to the left of FAB)
        panel_x = fab_x - self.quick_record_panel.width() + self.fab_quick_record.width()
        panel_y = fab_y - self.quick_record_panel.height() - 10 # 10px spacing from FAB

        # Ensure panel doesn't go off-screen (simple boundary check)
        if panel_x < 0: panel_x = 10
        if panel_y < 0: panel_y = 10

        self.quick_record_panel.move(panel_x, panel_y)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.position_quick_record_elements()
        # Ensure FAB is always on top
        self.fab_quick_record.raise_()
        if self.quick_record_panel.isVisible():
            self.quick_record_panel.raise_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = HabitFlowApp()
    sys.exit(app.exec_())
