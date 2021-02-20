<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md">
      <div class="q-gutter-y-md" style="min-width: 500px; max-width: 800px">
        <q-card>
          <q-tabs
            v-model="tab"
            dense
            class="text-grey"
            active-color="primary"
            indicator-color="primary"
            align="justify"
            narrow-indicator
          >
            <q-tab name="all" label="All"></q-tab>
            <q-tab name="only" label="Only"></q-tab>
            <q-tab name="random" label="Random"></q-tab>
          </q-tabs>

          <q-separator></q-separator>

          <q-tab-panels v-model="tab" animated>
            <q-tab-panel name="all">
              <div class="text-h6">All</div>
              <form @submit.prevent="simulateSubmit" class="q-pa-md">
                <q-input
                  filled
                  color="secondary"
                  hint="Type an ingredient"
                  v-model="test"
                ></q-input>
                <div class="row justify-end">
                  <q-btn
                    type="submit"
                    :loading="submitting"
                    label="Save"
                    class="q-mt-md"
                    color="secondary"
                  >
                    <template v-slot:loading>
                      <q-spinner-facebook></q-spinner-facebook>
                    </template>
                  </q-btn>
                </div>
              </form>
            </q-tab-panel>

            <q-tab-panel name="only">
              <div class="text-h6">Only</div>
              <q-input
                v-model="searchQuery"
                label="Label (stacked)"
                stack-label
              ></q-input>
              <div class="q-pa-md" style="max-width: 350px">
                <q-list>
                  <q-item>
                    <q-item-section>
                      <q-item-label>Single line item</q-item-label>
                      <q-item-label caption lines="2"
                        >Secondary line text. Lorem ipsum dolor sit amet,
                        consectetur adipiscit elit.</q-item-label
                      >
                    </q-item-section>

                    <q-item-section side top>
                      <q-item-label caption>5 min ago</q-item-label>
                      <q-icon name="star" color="yellow"></q-icon>
                    </q-item-section>
                  </q-item>

                  <q-separator spaced inset></q-separator>

                  <q-item>
                    <q-item-section>
                      <q-item-label>Single line item</q-item-label>
                      <q-item-label caption
                        >Secondary line text. Lorem ipsum dolor sit amet,
                        consectetur adipiscit elit.</q-item-label
                      >
                    </q-item-section>

                    <q-item-section side top>
                      <q-item-label caption>Voted!</q-item-label>
                    </q-item-section>
                  </q-item>

                  <q-separator spaced inset></q-separator>

                  <q-item>
                    <q-item-section>
                      <q-item-label>Single line item</q-item-label>
                      <q-item-label caption
                        >Secondary line text. Lorem ipsum dolor sit amet,
                        consectetur adipiscit elit.</q-item-label
                      >
                    </q-item-section>

                    <q-item-section side top>
                      <q-badge color="teal" label="10k"></q-badge>
                    </q-item-section>
                  </q-item>

                  <q-separator spaced inset></q-separator>

                  <q-item>
                    <q-item-section>
                      <q-item-label>Single line item</q-item-label>
                      <q-item-label caption
                        >Secondary line text. Lorem ipsum dolor sit amet,
                        consectetur adipiscit elit.</q-item-label
                      >
                    </q-item-section>

                    <q-item-section side top>
                      <q-item-label caption>2 min ago</q-item-label>
                      <div class="text-orange">
                        <q-icon name="star"></q-icon>
                        <q-icon name="star"></q-icon>
                        <q-icon name="star"></q-icon>
                      </div>
                    </q-item-section>
                  </q-item>

                  <q-separator spaced inset></q-separator>

                  <q-item>
                    <q-item-section>
                      <q-item-label>Single line item</q-item-label>
                      <q-item-label caption
                        >Secondary line text. Lorem ipsum dolor sit amet,
                        consectetur adipiscit elit.</q-item-label
                      >
                    </q-item-section>

                    <q-item-section side top>
                      <q-item-label caption>meta</q-item-label>
                    </q-item-section>
                  </q-item>
                </q-list>
              </div>
            </q-tab-panel>

            <q-tab-panel name="random">
              <div class="text-h6">Random</div>
              <q-btn
                label="New Smoothie"
                class="q-mt-md"
                color="secondary"
                @click="randomRecipe()"
              ></q-btn>
            </q-tab-panel>
          </q-tab-panels>
        </q-card>
        <q-card class="q-pa-md">
          <q-infinite-scroll @load="onLoad" :offset="250">
            <div
              v-for="(recipe, index) in recipes"
              :key="index"
              class="caption"
            >
              {{ recipe }}
            </div>
            <template v-slot:loading>
              <div class="row justify-center q-my-md">
                <q-spinner-dots color="primary" size="40px"></q-spinner-dots>
              </div>
            </template>
          </q-infinite-scroll>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
import recipeData from "../../data/recipes.json";

export default {
  name: "PageIndex",
  created() {
    this.allRecipes = recipeData;
  },
  data() {
    return {
      tab: "all",
      allRecipes: [],
      recipes: [],
      searchQuery: "",
      test: undefined, // this has something to do with search
      submitting: false,
    };
  },
  methods: {
    onLoad(index, done) {
      setTimeout(() => {
        // make this work in chunks for recipe loading
        // if (this.recipes) {
        //   this.recipes.push({}, {}, {}, {}, {}, {}, {});
        //   done();
        // }
      }, 2000);
    },
    randomRecipe() {
      const min = 0;
      const max = Math.floor(this.allRecipes.length);
      const choice = Math.floor(Math.random() * (max - min) + min);

      this.recipes = this.allRecipes[choice];
    },
    searchRecipes() {
      let results = [];
      let searchField = "name";
      let searchVal = "my Name";
      for (var i = 0; i < obj.list.length; i++) {
        if (obj.list[i][searchField] == searchVal) {
          results.push(obj.list[i]);
        }
      }
      this.recipes = results;
    },
  },
};
</script>
