## Tutorial of developing translation scripts
- Use [pyangbind](https://github.com/robshakir/pyangbind) to generate YANG bindings. 
- Use the framework utilities to generate translation script template.
- Developers implement their own translation scripts based on the template according to the YANG models in use
  - use the ```translate_edit_config_content``` API to accomplish the translation of ```edit-config``` operation
  - use the ```translate_query_filter_content``` API to accomplish the translation of ```get-config`` operation
