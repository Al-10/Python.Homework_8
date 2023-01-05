import view
import model
import logger

def run_calc():
    cont = 'yes'
    while cont == 'да' or cont == 'yes':
        mode = view.choose()
        if mode == '1':
            expr = view.get_expr()
            result = model.execute_expr(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
            cont = view.continue_work_calc()
        elif mode == '2':
            expr = view.get_expr()
            result = model.solve_eq(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
            cont = view.continue_work_calc()
        elif mode == '3':
            expr = view.get_expr()
            result = model.simpify_pol(expr)
            view.show_res(result)
            logger.log_exec(expr, result)
            cont = view.continue_work_calc()
        elif mode == '4':
            history = logger.get_history()
            view.show_history(history)
            cont = view.continue_work_calc()
        else:
            view.erorr_mode()
            cont = view.continue_work_calc()