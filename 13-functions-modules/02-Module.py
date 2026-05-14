#file module này là file thực thi người dùng sử dụng
#file này gọi các công cụ từ file mymodule ra đẻ tính toán số liệu thực tế


#import mymodule as mm bạn đang tạo một đường dây kết nối
#python sẽ tìm file mymodule trong cùng thư mục
#as mm giúp gọi tên file ngắn gọn hơn
import mymodule as mm#import la lien ket giua 2 file
addition = mm.sum(10,30)
subtraction = mm.subtract(30 , 5 )
dive = mm.divide(30 , 10 )
nul = mm.multiply(10,10)
print("SUM", addition)
print("SUBTRACT", subtraction)
print("DIVIDE", dive)
print("MULTIPLY", nul)


