import pickle as pk
file=open("lg.pkl","rb")
model= pk.load(file)
# --------- scaler--------
# file=open("scaler1.pkl","rb")
# scaler= pk.load(file)
# # ---------transform input------
# transform_data=scaler.transform([input])
def get_results(*labs):
    inputs=[float(i) for i in labs]
    return model.predict([inputs])