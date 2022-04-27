# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc
import requests 
from PIL import Image

base_url = "https://jobs.github.com/positions.json?description={}&location={}"

# Fxn to Retrieve Data
def get_data(url):
	resp = requests.get(url)
	return resp.json()


JOB_HTML_TEMPLATE = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
  border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h4>{}</h4>
<h5>{}</h5>
<h6>{}</h6>
</div>
"""

JOB_DES_HTML_TEMPLATE = """
<div style='color:#fff'>
{}
</div>
"""


def main():
	menu = ["Home","English","Hindi","Gujarati"]
	choice = st.sidebar.selectbox("Menu",menu)
	col1, col2, col3 = st.columns(3)
	with col1:
		st.write(' ')
	with col2:
		st.image("logo1.png")
	with col3:
		st.write(' ')


	if choice == "Home":

		# Nav  Search Form
		with st.form(key='searchform'):
			search_term = st.text_input("")
			col1, col2, col3,col4,col5 = st.columns(5)
			with col3:
				submit_search = st.form_submit_button(label='Search')
			


		# Results
		col1, col2 = st.columns([2,1])

		with col1:
			if submit_search:
				# Create Search Query
				search_url = base_url.format(search_term,location)
				# st.write(search_url)
				data = get_data(search_url)

				# Number of Results
				num_of_results = len(data)
				st.subheader("Showing {} jobs".format(num_of_results))
				# st.write(data)
		

				for i in data:
					job_title = i['title']
					job_location = i['location']
					company = i['company']
					company_url = i['company_url']
					job_post_date = i['created_at']
					job_desc = i['description']
					job_howtoapply = i['how_to_apply']
					st.markdown(JOB_HTML_TEMPLATE.format(job_title,company,job_location,job_post_date),
						unsafe_allow_html=True)

					# Description
					with st.expander("Description"):
						stc.html(JOB_DES_HTML_TEMPLATE.format(job_desc),scrolling=True)

					# How to Apply
					with st.expander("How To Apply"):
						# stc.html(job_howtoapply) # For White Theme
						stc.html(JOB_DES_HTML_TEMPLATE.format(job_howtoapply),scrolling=True) # For Dark Theme


		







	else:
		st.subheader("About")




if __name__ == '__main__':
	main()