
def statement_maker(full_statement:str):

    # full_statement = statement + sample_in + sample_out

    # with open ("./statement.txt", "r") as f:
    #     full_statement = f.read()

    # with open("./sample_in.txt", "r") as f:
    #     full_statement += "\nsample_in"
    #     full_statement += f.read()

    # with open("./sample_out.txt", "r") as f:
    #     full_statement += "\nsample_out"
    #     full_statement += f.read()

    # with open("full_in.txt", "r") as f:
    #     full_statement += "\ninput_to_execute"
    #     full_statement += f.read()

    full_statement = full_statement.replace('{', '').replace('}', '').replace('$', '').replace('&', '')
    return full_statement
 