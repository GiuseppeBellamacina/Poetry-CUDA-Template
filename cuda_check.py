import torch

def check_cuda():
    if torch.cuda.is_available():
        print("CUDA is available.")
        print("CUDA Version:", torch.version.cuda)
        print(f"Number of CUDA devices: {torch.cuda.device_count()}")
        for i in range(torch.cuda.device_count()):
            print(f"Device {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("CUDA is not available.")

if __name__ == "__main__":
    check_cuda()
