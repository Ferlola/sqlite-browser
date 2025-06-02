from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt
from src.UtilsSql.get_as_brackets import getAsBrackects
from src.UtilsSql.get_comillas import get_comillas


class CheckDataSelect(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.check_data()

    def check_data(self):
        self.current_text_list.clear()

        def datatable_select(self):
            try:
                self.current_text_list.append(
                    self.combobox_select_options.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_select(self)

        def datatable_select_sum(self):
            try:
                self.current_text_list.append(self.combobox_select_sum1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_sum1.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("*")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.number_edit.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_select_sum2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.combobox_select_sum1.currentText() != "select field":
                    self.current_text_list.append(self.label_prh3.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_sum2.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("AS")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                brackets = getAsBrackects(self.sum_as.text())
                self.current_text_list.append(brackets)
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_select_sum(self)

        def datatable_distinct(self):
            try:
                self.current_text_list.append(self.combo_distinct.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_distinct(self)

        def datatable_avg(self):
            try:
                self.current_text_list.append(self.combo_avg1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_avg.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("AS")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                brackets = getAsBrackects(self.lineedit_avg_as.text())
                self.current_text_list.append(brackets)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_avg2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_avg(self)

        def datatable_fields(self):
            try:
                self.current_text_list.append(self.itemsFields)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_fields1_count.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_all_fields2_count.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.lineedit_as.text():
                    brackets = getAsBrackects(self.lineedit_as.text())
                    self.current_text_list.append("AS " + brackets)
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_fields(self)

        def datatable_fields2(self):
            try:
                if self.itemsFieldsAll2:
                    itemsFieldsAll2 = self.itemsFieldsAll2
                    itemsFieldsAll2 = "," + itemsFieldsAll2
                    self.current_text_list.append(itemsFieldsAll2)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_fields2_count.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_all2_fields2_count.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.lineedit_as2.text():
                    brackets = getAsBrackects(self.lineedit_as2.text())
                    self.current_text_list.append("AS " + brackets)
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_fields2(self)

        def datatable_count(self):
            try:
                self.current_text_list.append(self.comboCount.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                text = self.count_lineedit_as.text()
                if text:
                    text = getAsBrackects(text)
                    text = "AS " + text
                    self.current_text_list.append(text)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_count_fields.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_count(self)

        def datatable_sum(self):
            try:
                self.current_text_list.append(self.combo_sum.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_as.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                brackets = getAsBrackects(self.line_edit.text())
                self.current_text_list.append(brackets)
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_sum(self)

        def datatable_case(self):
            try:
                state = self.checkbox_case.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append(", CASE WHEN")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_case_fields1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_case_operator1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_case_result_fields1.currentText()
                )
                self.current_text_list.append("THEN")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = get_comillas(self.case_lineedit1.text())
                self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.case_ombo_else1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_else_lineedit1.text()
                lineEdit = get_comillas(lineEdit)
                self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_end_as_lineedit1.text()
                if lineEdit:
                    lineEdit = get_comillas(lineEdit)
                    lineEdit = "END AS " + lineEdit
                    self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_case_fields2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_case_operator2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_case_result_fields2.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_lineEdit2.text()
                if lineEdit:
                    lineEdit = get_comillas(lineEdit)
                    lineEdit = "THEN " + lineEdit
                    self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.case_combo_else2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_else_lineedit2.text()
                lineEdit = get_comillas(lineEdit)
                self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_end_as_lineedit2.text()
                if lineEdit:
                    lineEdit = get_comillas(lineEdit)
                    lineEdit = "END AS " + lineEdit
                    self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_case_fields3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_case_operator3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_case_result_fields3.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_lineedit3.text()
                if lineEdit:
                    lineEdit = get_comillas(lineEdit)
                    lineEdit = "THEN " + lineEdit
                    self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_else_lineedit3.text()
                if lineEdit:
                    lineEdit = get_comillas(lineEdit)
                    lineEdit = " ELSE " + lineEdit
                    self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = self.case_end_as_lineedit3.text()
                if lineEdit:
                    lineEdit = get_comillas(lineEdit)
                    lineEdit = "END AS " + lineEdit
                    self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_case(self)

        def datatable_tables(self):
            try:
                self.current_text_list.append(self.combo_tables.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_tables_coma.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append(",")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_tables2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.limit_lineedit.text():
                    self.current_text_list.append("LIMIT ")
                    self.current_text_list.append(self.limit_lineedit.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_tables(self)

        def datatable_join(self):
            try:
                self.current_text_list.append(self.combo_join.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.combo_join_tables1.currentText():
                    joinTables1 = self.combo_join_tables1.currentText()
                    joinTables1 = joinTables1 + " ON "
                    self.current_text_list.append(joinTables1)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_join_tables2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_join_fields1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_join_tables3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_join_fields2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.combobox_join_tables4.currentText():
                    joinTables4 = self.combobox_join_tables4.currentText()
                    if joinTables4 == "Select table":
                        pass
                    else:
                        joinTables4 = "INNER JOIN " + joinTables4 + " ON "
                        self.current_text_list.append(joinTables4)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_join_tables5.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_join_fields3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_join_tables6.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_join_fields4.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_join(self)

        def datatable_where(self):
            try:
                self.current_text_list.append(self.combo_where_option.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_where_fields1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_where_exists_fields.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_where_operator.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_where_exists_from_tables1.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_result_query.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combobox_where_fields2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.items_where_combo_in)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_where_In_select_fields.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_result_between1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_exixts_where_tables1.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_where_in_select_tables.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_select_where_fields2.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_result_between2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_fields_select_avg.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = get_comillas(self.where_like_lineedit.text())
                self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_where_tables.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_exixts_where_fields1.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_select_tables.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_select_avg_tables.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_exixts_where_tables2.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                labelPrths1 = self.combobox_where_in_select_tables.currentText()
                labelPrths2 = self.combobox_where_in_select_where_fields.currentText()
                if labelPrths1 != "FROM table" and labelPrths2 == "Select WHERE":
                    self.current_text_list.append(")")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_where_exixts_where_fields2.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.where_select_label_prts.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                labelPrths1 = self.combo_where_exixts_where_fields3.currentText()
                labelPrths2 = self.combobox_where_exixts_where_fields2.currentText()
                if labelPrths1 == "AND field" and labelPrths2 != "Select field":
                    self.current_text_list.append(")")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combobox_where_in_select_where_fields.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_not_In_tables.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_select_where_field.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_where_exixts_where_fields3.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.comboWhereAnyWhereFields1.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_operator_select_where.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.comboOperatorAnyWhere.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_result_operator_select_where.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.comboResultOperatorAnyWhere.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_where(self)

        def datatable_and(self):
            try:
                self.current_text_list.append(self.combo_and.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_parenthesis1.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("(")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_fields1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_optr.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.items_and_in)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_fields3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_between1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_between2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = get_comillas(self.and_like_line_edit.text())
                self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_and(self)

        def datatable_and_or(self):
            try:
                self.current_text_list.append(self.combo_and_or.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_or_fields1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_or_optr1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_or_fields2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_or_fields3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.items_and_or_in)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_or_between1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_and_or_between2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                lineEdit = get_comillas(self.and_or_likeLineedit.text())
                self.current_text_list.append(lineEdit)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_parenthesis1.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append(")")
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_and_or(self)

        def datatable_groupby(self):
            try:
                state = self.checkbox_group_by.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("GROUP BY")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_group_by.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_groupby(self)

        def datatable_having(self):
            try:
                self.current_text_list.append(self.combo_having1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_having1_fields.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_having1_optrs1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.lineedit_having1.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_having2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_having2_fields.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_having2_optrs2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.lineedit_having2.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_having(self)

        def datatable_union(self):
            try:
                state = self.checkbox_union.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("UNION ")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_all.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("ALL ")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                state = self.checkbox_union.checkState()
                if state == Qt.CheckState.Checked:
                    self.current_text_list.append("SELECT ")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.itemsUnion)
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.itemsUnion:
                    self.current_text_list.append("FROM ")
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.union_tables.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                if self.union_where_combo.currentText() != "WHERE field":
                    self.current_text_list.append("WHERE ")
                    self.current_text_list.append(self.union_where_combo.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_union_operator.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.union_operator.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_union(self)

        def datatable_orderby(self):
            try:
                self.current_text_list.append(self.combo_order_by1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_order_by_avg.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_avg_asc.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_order_by2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_asc1.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_order_by3.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.combo_asc2.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_having_case_fields1.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(
                    self.combo_having_case_fields2.currentText()
                )
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                current_text = self.combo_having_case_fields1.currentText()
                current_field = current_text.replace("WHEN ", "")
                current_field = current_field.replace(" IS NULL ", "")
                self.current_text_list.append("ELSE " + current_field + " END)")
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_orderby(self)

        def datatable_top(self):
            try:
                self.current_text_list.append(self.topLineEdit.text())
            except (AttributeError, RuntimeError) as e:
                print(e)

            try:
                self.current_text_list.append(self.topcomboFields.currentText())
            except (AttributeError, RuntimeError) as e:
                print(e)

        datatable_top(self)

        return self.current_text_list
