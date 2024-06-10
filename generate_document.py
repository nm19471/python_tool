import sys

def generate_document(user_input):
    output_filename = f'document_{user_input}.txt'
    with open(output_filename, 'w') as f:
        f.write(f"Document generated with input: {user_input}")
    print(f"Document {output_filename} generated successfully!")

if __name__ == "__main__":
    user_input = sys.argv[1]
    generate_document(user_input)
