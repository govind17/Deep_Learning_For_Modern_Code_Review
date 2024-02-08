As part of the Deep Learning for Modern Code Review course, 
the original model present here: https://github.com/sjj0403/GSCS was tested against code review task.

# Dependent software libraries are mentioned in requiremets.txt file

# GPU is required for training.

# Dataset
I conducted experiments on three different public dataset on the task of code summarization.
1. The Hu dataset for code summarization can be accessible from the paper https://arxiv.org/abs/2005.00653
2. The ETCR code review dataset can be accessible from the paper https://cse.cs.ovgu.de/cse/exploit-those-code-reviews-bigger-data-for-deeper-learning-17/
3. The Tufano's code review dataset can be accessible from the paper https://dl.acm.org/doi/abs/10.1145/3510003.3510621
# Run the code
1. To different dataset, you can change its parameter setting in the file gscs/config.py.
2. To train the model, you can set the main function to run _train() in the file gscs/main.py.
3. To test the model, you can set the main function to run _test() and set the picked model file's path in the file gscs/main.py.
4. To evaluate the result, you can use three metrics in the floder evaluation.
