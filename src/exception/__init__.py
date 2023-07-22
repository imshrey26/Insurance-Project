import os
import sys


class InsuranceException(Exception):

    def __init__(self,error_message:Exception,error_detail:sys):
        super().__init__(error_message)
        self.error_message = InsuranceException.error_message_detail(error_message,error_detail=error_detail)
        
    @staticmethod
    def error_message_detail(error: Exception,error_detail:sys)->str:
        _,_,exc_tb = error_detail.exc_info()

        # Extracting the line number where exception has occured
        exception_block_line_number = exc_tb.tb_frame.f_lineno
        try_block_line_number = exc_tb.tb_lineno

        # Extracting the filename where the exception has occured
        file_name = exc_tb.tb_frame.f_code.co_filename

        # Preparing error message
        error_message = f"""
        Error occured in execution of :
        [{file_name}] at
        try block line number : [{try_block_line_number}]
        and exception block line number : [{exception_block_line_number}]
        error message : [{error_message}]
        """
        return error_message
    
    def __str__(self):
        """
        Formating how a object should be visible if used in print statement.
        """
        return self.error_message


    def __repr__(self):
        """
        Formating object of AppException
        """
        return InsuranceException.__name__.__str__()