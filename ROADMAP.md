# CV Platform Roadmap — building a thin Roboflow, solo

A solo build of a computer-vision platform (a stripped-down Roboflow), grown one shippable feature at a time.

- **Pace:** ~10–15 hrs/week
- **Cadence:** one increment every two weeks
- **North star:** a multi-user platform that lets you upload images, label them, train a model, deploy it, and monitor it — reached the de-risked way, one vertical slice at a time.

---

## How to use this file

- **Ship at the fortnight boundary, even if it's ugly.** Tag the version, write one changelog line, push.
- **One shippable feature per version.** If an increment is secretly two, it's scoped wrong.
- **Cut scope before extending time.** Shrinking the slice is the core solo skill.
- **Build in public.** Post each version somewhere (LinkedIn / dev log). With no teammate, this is your accountability — and it doubles as your recruiter-facing story.
- **Learn just-in-time.** Read each version's doc *when you reach it*, not before.

## Definition of done (applies to every version)

- [ ] Feature works end to end
- [ ] Committed, tagged `v0.0.x`, pushed
- [ ] One-line entry added to `CHANGELOG.md`
- [ ] Short public post or dev-log note written

---

## Phase 1 — Make it work  (weeks 1–6)
*Goal: a living thing on the internet that does one useful CV task. Resist architecting.*

### v0.0.1 — Upload → predict → show, deployed live
- [ ] Upload an image, run one pretrained model, display the result
- [ ] Live public URL
- **Skill:** app structure, model inference, deployment
- **Learn:** Gradio quickstart; Hugging Face Spaces docs

### v0.0.2 — Persist uploads + predictions, add a history page
- [ ] Save each upload and its prediction to a database
- [ ] A page that lists past results
- **Skill:** data persistence (this is what turns a demo into an application)
- **Learn:** Python `sqlite3` basics (or SQLModel for a gentler ORM)

### v0.0.3 — Model selection + confidence scores
- [ ] User can choose between 2–3 models
- [ ] Show top predictions with confidence
- **Skill:** treating the model as swappable config instead of hard-coding it
- **Learn:** Hugging Face `pipeline` interface

---

## Phase 2 — Productionize  (weeks 7–12)
*Goal: the same app, shaped like real software. This phase is your MLOps signal.*

### v0.0.4 — Split backend from frontend
- [ ] FastAPI backend that serves inference
- [ ] Thin frontend that calls the API
- **Skill:** separation of concerns, API-first design (the most important architectural lesson here)
- **Learn:** FastAPI official tutorial

### v0.0.5 — Containerize with Docker
- [ ] Dockerfile for the backend (and frontend)
- [ ] Whole stack runs via `docker compose`
- **Skill:** containerization
- **Learn:** Docker "Get started"; Dockerfile best practices

### v0.0.6 — CI/CD with GitHub Actions
- [ ] Tests run automatically on every push
- [ ] Image builds (and deploys) on push
- **Skill:** automation + your first real tests
- **Learn:** GitHub Actions quickstart; pytest intro
- *After this, the repo runs itself — a senior habit in a junior portfolio.*

---

## Phase 3 — Platform core  (weeks 13–22)
*Goal: the end-to-end pipeline wearing a UI. Now it earns the word "platform."*

### v0.0.7 — Projects / datasets
- [ ] Group uploaded images into named collections
- **Skill:** data modeling, relational design
- **Learn:** database relationships basics (one-to-many)

### v0.0.8 — Annotation view  *(hardest single increment — give it the full fortnight)*
- [ ] Draw bounding boxes on an image
- [ ] Save the labels
- **Skill:** frontend interactivity, label formats
- **Learn:** YOLO label format (just text files); HTML canvas basics
- *Scope guard: bounding boxes only. No polygons, no keyboard shortcuts yet.*

### v0.0.9 — Dataset export
- [ ] Export a labeled dataset as a standard YOLO/COCO zip
- **Skill:** data export, format conversion
- **Learn:** COCO/YOLO dataset structure

### v0.1.0 — Fine-tune on a user's dataset  *(milestone: the platform now trains, not just uses)*
- [ ] Train/fine-tune a model on uploaded labeled data
- **Skill:** transfer learning, training loops
- **Learn:** Ultralytics YOLO training docs

### v0.1.1 — Experiment tracking
- [ ] Log metrics and parameters for every training run
- [ ] View runs in the UI
- **Skill:** experiment tracking, reproducibility
- **Learn:** MLflow tracking (or Weights & Biases quickstart)

---

## Phase 4 — Real platform  (weeks 23+)
*Goal: polish that turns a project into a product story.*

### v0.1.2 — Model registry
- [ ] Choose which trained version the inference API serves
- **Skill:** model versioning
- **Learn:** MLflow Model Registry

### v0.1.3 — Monitoring
- [ ] Log production predictions
- [ ] Flag confidence drops / drift
- **Skill:** drift detection (this is where the lab-vs-field failure mode finally gets caught)
- **Learn:** Evidently AI intro

### v0.2.0 — Auth + multi-user
- [ ] Authentication
- [ ] Each user sees only their own projects
- **Skill:** auth, multi-tenancy
- **Learn:** FastAPI security / OAuth2 tutorial
- *After this: a genuine multi-user CV platform — the north star.*

---

## Build-in-public log
*Add a line per shipped version — date, version, one thing you learned. This becomes your portfolio narrative.*

| Date | Version | What I shipped | One thing I learned |
|------|---------|----------------|---------------------|
|      | v0.0.1  |                |                     |
