import streamlit as st
import pickle

# Load the model
with open('rf.pkl', 'rb') as load:
    model = pickle.load(load)

st.title('BANKRUPTCY PREDICTION')
#st.markdown('USING MACHINE LEARNING')
st.image("https://img.freepik.com/premium-vector/vector-illustration-finance-savings-concept-suitable-various-purposes_675567-5822.jpg",width=300)
# Prediction function
def predict(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
    prediction = model.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    return prediction

def main():
    st.markdown("### ENTER THE DETAILS")

    # Input fields
    industrial_risk = st.number_input('Industrial Risk:', min_value=0.0, max_value=10.0, step=0.5)
    management_risk = st.number_input('Management Risk:', min_value=0.0, max_value=10.0, step=0.5)
    financial_flexibility = st.number_input('Financial Flexibility:', min_value=0.0, max_value=10.0, step=0.5)
    credibility = st.number_input('Credibility:', min_value=0.0, max_value=10.0, step=0.5)
    competitiveness = st.number_input('Competitiveness:', min_value=0.0, max_value=10.0, step=0.5)
    operating_risk = st.number_input('Operating Risk:', min_value=0.0, max_value=10.0, step=0.5)

    # Prediction button
    if st.button('Predict'):
        result = predict(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)
        if result[0] == 0:  # Assuming the model returns [0] for Bankruptcy
            st.success("Prediction: Bankruptcy")
        else:
            st.success("Prediction: Non-Bankruptcy")

if __name__ == '__main__':
    main()
