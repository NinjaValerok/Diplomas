from write_read_files.write_read_files import *
from PCA_stuff.PCA import *




class Controller:
    @staticmethod
    def get_matrix_T_P(file):
        T = np.array(parse_csv('files/' + file.get_name_PCA_file_T()), dtype=np.float64)
        P = np.array(parse_csv('files/' + file.get_name_PCA_file_P()), dtype=np.float64)
        return T,P


    @staticmethod
    def load_file_and_calculate_PCA(file):
        row_matrix = parse_xml('files/' + file.__str__())
        T,P = calculate_PCA_SVD(row_matrix)
        write_csv_list('files/'+ file.get_name_PCA_file_T(),T.tolist())
        write_csv_list('files/'+ file.get_name_PCA_file_P(),P.tolist())
        return T,P