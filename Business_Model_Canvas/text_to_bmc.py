import ast
import openai
from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')


openai.api_key = "sk-NCl9ebUEbOu1T3BlbkFJ1peagkXsv2N2bOuvr1RI"

# insert your text here
text = '''Well, if I were to bring this idea to life, I think there could be a significant demand for a password-keeping watch, especially among individuals who value security and convenience. I could potentially market this watch to professionals, entrepreneurs, and other individuals who need to manage a lot of passwords for work or personal use.

In terms of pricing, I would have to consider the costs of manufacturing, marketing, and distribution. Since this would be a niche product, I would likely need to price it higher than a traditional watch to make a profit. However, I would have to strike a balance between affordability and profitability to make sure the product is accessible to a wider range of customers.

I think the key to success would be a strong marketing strategy, particularly in the digital space. I would need to create a buzz around the product and highlight its unique features to stand out from other smartwatches on the market. I would also need to partner with key influencers and thought leaders to promote the product and generate interest.

In terms of costs, I would need to factor in the costs of research and development, manufacturing, marketing, and distribution. I would also need to consider the costs of ongoing support and maintenance for the product.
'''

def generate_bmc_dictionary(text):

    prompt = (
        f"take the given text:\n\n{text}\n\n"
        "Make a Business Model Canvas based on the text above. Give as an output: python dictionary format with following keys and values as the list of strings. Each point ___ must have 3-10 word description: \n"
        '{"key_partners": ["___",  "___", "___"], "key_activities": ["___",  "___", "___"], "key_resources": ["___",  "___", "___"], "value_propositions": ["___",  "___", "___"], "customer_relationships": ["___",  "___", "___"], "channels": ["___",  "___", "___"], "customer_segments": ["___",  "___", "___"], "cost_structure": ["___",  "___", "___"], "revenue_streams": ["___",  "___", "___"]})'
    )

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    bmc_dictionary = ast.literal_eval(response.choices[0].text.strip())
    print(bmc_dictionary)
    return bmc_dictionary


@app.route('/')
def bmc():
    bmc_data = generate_bmc_dictionary(text)
    return render_template('bmc.html', bmc=bmc_data)
    


if __name__ == '__main__':
    app.run(debug=True)