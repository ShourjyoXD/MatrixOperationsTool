import streamlit as st
import numpy as np

# Matrix Operations
def add_matrices(A, B):
    return np.add(A, B)

def subtract_matrices(A, B):
    return np.subtract(A, B)

def multiply_matrices(A, B):
    return np.dot(A, B)

def transpose_matrix(A):
    return np.transpose(A)

def determinant_matrix(A):
    return np.linalg.det(A)

# Streamlit UI
st.title("Matrix Operations Tool")

st.sidebar.header("Matrix Input")
rows = st.sidebar.number_input("Enter number of rows:", min_value=1, max_value=5, value=2)
cols = st.sidebar.number_input("Enter number of columns:", min_value=1, max_value=5, value=2)

matrix1 = np.zeros((rows, cols))
matrix2 = np.zeros((rows, cols))

st.sidebar.subheader("Enter values for Matrix A:")
for i in range(rows):
    for j in range(cols):
        matrix1[i][j] = st.sidebar.number_input(f"A[{i+1}][{j+1}]", value=0.0)

st.sidebar.subheader("Enter values for Matrix B:")
for i in range(rows):
    for j in range(cols):
        matrix2[i][j] = st.sidebar.number_input(f"B[{i+1}][{j+1}]", value=0.0)

operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Transpose A", "Determinant A"])

if st.button("Compute"):
    st.write("### Matrix A:")
    st.write(matrix1)

    st.write("### Matrix B:")
    st.write(matrix2)

    if operation == "Addition":
        result = add_matrices(matrix1, matrix2)
        st.write("### Result (A + B):")
        st.write(result)

    elif operation == "Subtraction":
        result = subtract_matrices(matrix1, matrix2)
        st.write("### Result (A - B):")
        st.write(result)

    elif operation == "Multiplication":
        result = multiply_matrices(matrix1, matrix2)
        st.write("### Result (A * B):")
        st.write(result)

    elif operation == "Transpose A":
        result = transpose_matrix(matrix1)
        st.write("### Result (Transpose of A):")
        st.write(result)

    elif operation == "Determinant A":
        if rows == cols:
            result = determinant_matrix(matrix1)
            st.write("### Result (Determinant of A):")
            st.write(result)
        else:
            st.write("⚠️ Determinant is only for square matrices!")



