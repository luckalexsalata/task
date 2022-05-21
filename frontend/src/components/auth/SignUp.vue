  <template>
   <div class="w-50 border rounded p-3 mx-auto">
     <b-form @submit="register">
       <div class="form-group required">
         <label for="username">Login:</label>
         <b-input v-model="username" type="text" id="username" placeholder="Логин..."></b-input>
       </div>
       <div class="form-group required">
         <label for="employeeOrOwner">Are you an employee or owner?</label>
         <b-select v-model="employeeOrOwner" :options="employeeOrOwnerOptions" type="employeeOrOwner" id="employeeOrOwner">
         </b-select>
       </div>
       <div class="form-group required">
         <label class="control-label" for="password">Password:</label>
         <b-input v-model="password" type="password" id="password" placeholder="password..."></b-input>
       </div>
       <div class="form-group required">
         <label for="repeatPassword">Repeate password:</label>
         <b-input v-model="repeatPassword" type="password" id="repeatPassword" placeholder="Repeate password..."></b-input>
       </div>
       <p class="text-danger" v-if="!$v.password.minLength">Password length is less than 8 characters</p>
       <p class="text-danger" v-if="$v.password.required && $v.repeatPassword.required && !$v.repeatPassword.sameAs">
        The entered passwords do not match.
       </p>
       <b-button variant="primary" type="submit" :disabled="formValid">Registration</b-button>

       <p class="mt-3">Уже есть аккаунт? <router-link to="/auth/signin">Login</router-link>
       </p>
     </b-form>
   </div>
  </template>
  <script>
  import { required, minLength, sameAs } from 'vuelidate/lib/validators'

  export default {
    name: 'SignUp',
    data() {
      return {
        username: '',
        password: '',
        repeatPassword: '',
        phone: '',
        employeeOrOwner: '',
        employeeOrOwnerOptions: [
          { text: 'Select...', value: '', disabled: true, selected: true },
          { text: 'Owner', value: 'owner' },
          { text: 'employee', value: 'employee' }
        ]
      }
    },
    validations: {
      username: {
        required,
        minLength: minLength(4)
      },
      password: {
        required,
        minLength: minLength(8)
      },
      repeatPassword: {
        required,
        sameAs: sameAs('password')
      },
      employeeOrOwner: {
        required
      }
   },
   computed: {
     formValid() {
        return this.$v.$invalid
     }
   },
    methods: {
      register(event) {
        event.preventDefault()
        this.axios
          .post(`http://localhost:8000/api/user/auth/users/`, { headers: {'Content-type': 'application/json'},
            'username': this.username,
            'password': this.password })
          .then(response => { this.$router.push('/auth/signin') })
          .catch(err => { console.error(err) })
      }
    }
  }

  </script>
  <style>
  </style>
