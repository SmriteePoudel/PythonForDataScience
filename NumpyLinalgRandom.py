{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "378c18a9-d8de-4648-8fdb-c57a2b2984fc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Matrix A:\n",
      " [[4 1 7]\n",
      " [3 4 9]\n",
      " [2 7 9]]\n",
      "Matrix B:\n",
      " [[7 1 2]\n",
      " [5 7 3]\n",
      " [9 9 6]]\n",
      "Dot Product:\n",
      " [[ 96  74  53]\n",
      " [122 112  72]\n",
      " [130 132  79]]\n",
      "Vector Product:\n",
      " [[ -5  41  -3]\n",
      " [-51  36   1]\n",
      " [-39  69 -45]]\n",
      "Inner Product:\n",
      " [[ 43  48  87]\n",
      " [ 43  70 117]\n",
      " [ 39  86 135]]\n",
      "Matrix Multiplication:\n",
      " [[ 96  74  53]\n",
      " [122 112  72]\n",
      " [130 132  79]]\n",
      "Determinant of A: -25.99999999999999\n",
      "Sum of Diagonal Elements of A: 17\n",
      "Inverse of A:\n",
      " [[ 1.03846154 -1.53846154  0.73076923]\n",
      " [ 0.34615385 -0.84615385  0.57692308]\n",
      " [-0.5         1.         -0.5       ]]\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "# Generate two random arrays\n",
    "A = np.random.randint(1, 10, size=(3, 3))\n",
    "B = np.random.randint(1, 10, size=(3, 3))\n",
    "\n",
    "# Compute dot product, vector product, and inner product\n",
    "dot_product = np.dot(A, B)\n",
    "vector_product = np.cross(A, B)\n",
    "inner_product = np.inner(A, B)\n",
    "\n",
    "print(\"Matrix A:\\n\", A)\n",
    "print(\"Matrix B:\\n\", B)\n",
    "print(\"Dot Product:\\n\", dot_product)\n",
    "print(\"Vector Product:\\n\", vector_product)\n",
    "print(\"Inner Product:\\n\", inner_product)\n",
    "\n",
    "# Matrix operations\n",
    "matrix_multiplication = np.matmul(A, B)\n",
    "determinant_A = np.linalg.det(A)\n",
    "sum_diagonal_A = np.trace(A)\n",
    "inverse_A = np.linalg.inv(A) if determinant_A != 0 else \"Not invertible\"\n",
    "\n",
    "print(\"Matrix Multiplication:\\n\", matrix_multiplication)\n",
    "print(\"Determinant of A:\", determinant_A)\n",
    "print(\"Sum of Diagonal Elements of A:\", sum_diagonal_A)\n",
    "print(\"Inverse of A:\\n\", inverse_A)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed87dc4f-8769-4a5f-99cd-678259321a73",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
