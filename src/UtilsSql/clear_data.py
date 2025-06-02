from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt


class ClearDataSelect(QWidget):
    def __init__(self):
        super().__init__()
        self.clear_data()

    def clear_column_combo_fields2_in(self):
        try:
            model = self.combo_fields2.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                item.setFlags(
                    Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable
                )
                item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        except (AttributeError, RuntimeError) as e:
            print(e)

    def clear_column_combo_fields1_in(self):
        try:
            model = self.combo_fields1.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                item.setFlags(
                    Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable
                )
                item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        except (AttributeError, RuntimeError) as e:
            print(e)

    def clear_column_combo_where_in(self):
        try:
            model = self.combo_where_in.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                item.setFlags(
                    Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable
                )
                item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        except (AttributeError, RuntimeError) as e:
            print(e)

    def clear_column_combobox_and_in(self):
        try:
            model = self.combobox_and_in.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                item.setFlags(
                    Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable
                )
                item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        except (AttributeError, RuntimeError) as e:
            print(e)

    def clear_column_comboitems_and_or_in(self):
        try:
            model = self.combobox_and_or_in.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                item.setFlags(
                    Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable
                )
                item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        except (AttributeError, RuntimeError) as e:
            print(e)

    def clear_column_combo_union_in(self):
        try:
            model = self.union_select_combo.model()
            for index in range(model.rowCount()):
                item = model.item(index)
                item.setFlags(
                    Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsUserCheckable
                )
                item.setData(Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        except (AttributeError, RuntimeError) as e:
            print(e)

    def clear_data(self):

        def clear_data_table_select(self):
            try:
                self.combobox_select_options.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_select(self)

        def clear_data_table_select_sum(self):
            try:
                self.combobox_select_sum1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox1.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox1.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.number_edit.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combobox_select_sum2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.sum_as.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_select_sum(self)

        def clear_data_table_distinct(self):
            try:
                self.combo_distinct.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_distinct(self)

        def clear_data_table_avg(self):
            try:
                self.combo_avg1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_avg.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_avg.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.avgAs.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_avg2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_avg(self)

        def clear_data_table_fields(self):
            try:
                self.combo_all_fields2_count.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineedit_as.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_fields(self)

        def clear_data_table_fields2(self):
            try:
                self.line_edit2.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboCount.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_as.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.line_edit.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_fields2(self)

        def clear_data_table_tables(self):
            try:
                self.combo_tables.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditTables1.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_tables_coma.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_tables_coma.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_tables2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditTables2.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_tables(self)

        def clear_data_table_case(self):
            try:
                state = self.checkbox_case.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_case.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_case(self)

        def clear_data_table_join(self):
            try:
                self.combo_join.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_join_tables1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_join_tables2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combobox_join_fields1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_join_tables3.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combobox_join_fields2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_join(self)

        def clear_data_table_where(self):
            try:
                self.combo_where_option.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboWhereNoExixtsTables.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboWhereNoExixtsWhereTables1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboWhereNoExixtsWhereFields1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboWhereNoExixtsWhereTables2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboWhereNoExixtsWhereFields2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combobox_where_fields1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_where_operator.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_result_query.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combobox_where_fields2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combobox_fields_select_avg.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_select_avg_tables.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_result_between1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_result_between2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_where_tables.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_where(self)

        def clear_data_table_and(self):
            try:
                self.combo_and.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkboxAnd.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkboxAnd.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_parenthesis1.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_parenthesis1.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditAnd1.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_fields1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_optr.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditAnd2.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_fields3.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_between1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_between2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditLike3.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkboxUnderscore1.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkboxUnderscore1.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditLike4.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_fields3.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditLike6.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_parenthesis1.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_parenthesis1.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_and(self)

        def clear_data_table_and_or(self):
            try:
                self.combo_and_or.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_or_fields1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_or_optr1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_or_fields2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_or_fields3.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.lineEditLike5.clear()
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkboxUnderscore2.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkboxUnderscore2.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_or_between1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_and_or_between2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_and_or(self)

        def clear_data_table_groupby(self):
            try:
                state = self.checkbox_group_by.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_group_by.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_group_by.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_groupby(self)

        def clear_data_table_having(self):
            try:
                self.combo_having1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_having1_fields.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_having1_optrs1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboHaving1optrsResult.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_having2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_having2_fields.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_having2_optrs2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.comboHaving2optrsResult.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_having(self)

        def clear_data_table_union(self):
            try:
                state = self.checkbox_union.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_union.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_all.checkState()
                if state == Qt.CheckState.Checked:
                    self.checkbox_all.setChecked(False)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.union_tables.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.union_where_combo.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_union_operator.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.union_operator.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_union(self)

        def clear_data_table_orderby(self):
            try:
                self.combo_order_by1.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_order_by_avg.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_avg_asc.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_order_by2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.combo_asc2.setCurrentIndex(0)
            except (AttributeError, RuntimeError) as e:
                print(e)

        clear_data_table_orderby(self)
