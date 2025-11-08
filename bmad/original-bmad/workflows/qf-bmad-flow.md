# BMAD Complete Process Flow - QuantumNotary Orchestration

This specialization adapts the BMAD orchestration template for the **QuantumNotary** API service that anchors notarization proofs on the emerging **quantumFusion** network. The BMAD Master remains project-agnostic but prioritizes distributed-ledger workflows, Substrate/Polkadot VM runtime safety, and SQLAlchemy-backed API state.

## CRITICAL: BMAD Master Coordination Protocol

**🎯 BMAD MASTER IS THE AIR-TRAFFIC CONTROLLER FOR QUANTUMNOTARY DELIVERY CYCLES**

### BMAD Master Orchestration Framework

**BMAD Master** keeps holistic control across on-chain and off-chain workstreams to guarantee notarization guarantees remain verifiable end-to-end.

#### Story Initiation and Decomposition
- **Story Analysis**: Capture notarization flows, ledger dependencies, signing authorities, and data retention rules.
- **Task Breakdown**: Split stories into on-chain runtime work, API/interface work, SQLAlchemy data migrations, and operational dependencies with clear artifacts.
- **Agent Selection**: Activate only the specialists required for the current ledger/API change set.
- **Dependency Mapping**: Track critical sequencing (e.g., runtime upgrade → API contract update → DB migration).
- **Risk & Compliance Callouts**: Flag cryptography, custody, or regulatory considerations so agents can align on mitigations.

#### Specialist Agent Delegation Structure
BMAD Master centers these specialists around web3, experimental blockchain, and API expertise:
- 🧭 **Web3 Protocol Architect** – Defines quantumFusion RPC usage, transaction semantics, and notarization finality rules.
- 🛰️ **Substrate Runtime Engineer** – Designs and maintains Substrate pallets, Polkadot VM weight configurations, and runtime upgrades.
- 🌐 **QuantumFusion Network Specialist** – Manages the `quantumFusion` repo, chain specs, dev/testnet bootstrapping, artifact packaging, and rollout scripts.
- 🧪 **Polkadot VM Safety Auditor** – Verifies Wasm artifacts, runtime metadata compatibility, and upgrade rollback plans.
- 🔌 **API & Gateway Specialist** – Owns REST/gRPC contracts, idempotency design, auth layers, and external partner integrations.
- 🎨 **Frontend Experience Specialist** – Designs and implements signup/home/dashboard UX, ensuring accessibility, responsiveness, and trust cues.
- 🗃️ **SQLAlchemy & State Steward** – Maintains DB schemas, ORM models, connection pools, and migration health.
- 🔐 **Cryptography & Key Management Specialist** – Handles signer custody, HSM/in-memory key usage, and secure envelope serialization.
- 📡 **Network & Observability Engineer** – Monitors node health, RPC endpoints, telemetry, and incident response runbooks.
- ⚙️ **QA & Simulation Agent** – Builds deterministic simulations, property-based tests, fuzzing scenarios, and ledger/API regression suites.

#### Master Orchestration Responsibilities
1. **📋 Master Todo Management**: Maintain dependency-aware todos across ledger, API, database, and infrastructure tracks.
2. **🔄 Task Coordination**: Sequence runtime vs. API deployments, ensuring migrations and RPC changes ship in the proper order.
3. **📡 Network Awareness**: Confirm quantumFusion devnet/testnet status before green-lighting specialist work.
4. **🧠 Knowledge Integration**: Fuse outputs from Substrate, API, SQLAlchemy, and Frontend specialists into cohesive delivery packages.
5. **🚨 Quality Gate Enforcement**: Enforce ledger/API/UI guardrails, signing safety, and rollout checklists.
6. **📊 Progress Consolidation**: Publish multi-agent status updates covering off-chain + on-chain + UI readiness.
7. **🎨 Customer Experience Alignment**: Ensure stories addressing onboarding/home/dashboard flows include UX specs, component references, and content decisions.
8. **📁 Epic Organization**: Maintain epic/story structure and ensure artifacts are archived for auditability.

#### Epic Creation and Organization Standards
**MANDATORY for all epic creation processes (adjust the base path when importing into `~/Documents/qfProjects/quantumNotary`)**

- **Epic Storage Location**: `/Users/michaelulrich/Documents/qfProjects/quantumNotary/bmad/epics/[epic-name]/`
- **Epic Directory Structure**:
  ```
  /quantumNotary/bmad/epics/[epic-name]/
  ├── epic-overview.md
  └── stories/
      ├── story-[epic-name]-001-[story-name].md
      ├── story-[epic-name]-002-[story-name].md
      └── ...
  ```
- **Story Organization**: All stories tied to an epic stay inside its `/stories/` directory for context continuity.
- **Naming Conventions**: Keep kebab-case directories and `story-[epic-name]-[number]-[story-name].md` file names for traceability.

#### Specialist Agent Handoff Protocol
```
BMAD Master → Ledger/API Story Analysis → Specialist Assignment → Task Delegation → Progress & Network Monitoring → Quality Verification → Integration → Delivery
```

**Each handoff includes:**
- Explicit ledger contract/runtime expectations (RPC endpoints, pallet version, blocktime assumptions).
- API contract details (request/response schemas, auth scopes, rate limits).
- SQLAlchemy migration plan, rollback instructions, and seed data needs.
- Frontend UX/UI specs, component references, and accessibility considerations tied to the story.
- Security & compliance expectations (signing keys, audit artifacts, threat models).
- Reporting cadence and deliverable formats (PRs, runtime artifacts, dashboards).

## CRITICAL: QuantumNotary API & Network Integrity Requirements

Protecting notarization correctness requires synchronized validation of the API service, SQLAlchemy persistence, and the quantumFusion network. No specialist may proceed without proving the foundation is healthy.

### Phase 0: Mandatory QuantumNotary Pre-Flight (Before Any Work)

1. **QuantumFusion Node & RPC Health**
   - From `~/Documents/quantumFusion`, start or confirm the devnet/testnet node is running (e.g., `make devnet` or the project’s provided script).
   - Verify RPC responsiveness and chain metadata:
     ```bash
     cd ~/Documents/quantumFusion
     curl -H "Content-Type: application/json" \
          -d '{"id":1,"jsonrpc":"2.0","method":"system_health","params":[]}' \
          http://localhost:9944
     ```
   - Record the runtime spec version and commit hash used for this cycle.

2. **API Dependency & Smoke Test**
   - Bootstrap/refresh the Python environment for `~/Documents/qfProjects/quantumNotary`.
   - Confirm dependencies install cleanly, then run the fastest green test target before making changes:
     ```bash
     cd ~/Documents/qfProjects/quantumNotary
     python -m venv .venv && source .venv/bin/activate
     pip install -r requirements.txt
     pytest tests/smoke --maxfail=1 --disable-warnings
     ```
   - Document the API entry point (e.g., `uvicorn quantum_notary.api:app`) and ensure it starts with current env vars.

3. **SQLAlchemy Migration Baseline**
   - Ensure `DATABASE_URL` (or equivalent) points to the correct instance.
   - Validate schema alignment and stamp the current revision:
     ```bash
     cd ~/Documents/qfProjects/quantumNotary
     alembic upgrade head
     alembic current
     ```
   - If migrations are pending, resolve them before specialists touch application code.

4. **Runtime/Artifact Alignment**
   - Sync Substrate runtime artifacts (Wasm, metadata) between `quantumFusion` and the API repo.
   - Store the artifact checksums alongside the story or epic so agents know which version to target.

5. **Secrets & Signing Assets**
   - Verify access to keystores, mnemonic vaults, or HSM endpoints required for notarization.
   - Confirm that non-production keys are clearly labeled and production keys are inaccessible in dev contexts.

**❌ STOP IMMEDIATELY if any pre-flight step fails.** BMAD Master must coordinate remediation before assigning work.

### Phase 8.12: Mandatory Post-Work Verification (After Any Work)

1. **Regression & Simulation Tests**
   - Re-run `pytest` (unit + integration) plus any deterministic simulations or fuzzers that cover the touched modules.
   - Add ledger-in-the-loop checks (e.g., submit a dry-run notarization transaction against the devnet).

2. **Frontend Regression & Visual Checks**
   - Execute component/unit tests plus UI automation suites (Playwright/Cypress) covering signup, home, and notarization flows.
   - Run Lighthouse or equivalent performance/accessibility scans; document notable deltas.
   - Provide updated screenshots or recordings for Product/Legal review when flows change.

3. **Database & Migration Integrity**
   - Execute `alembic upgrade head` and `alembic downgrade -1` (if safe) to prove migrations are reversible.
   - Inspect SQLAlchemy models for drift (`alembic revision --autogenerate --head head --rev-id verify` or equivalent) and ensure there is no unintended diff.

4. **API & RPC Smoke Run**
   - Launch the API with the updated code (`uvicorn ...`) and hit the notarization endpoints using a canned request.
   - Check RPC health again to make sure runtime upgrades or metadata changes didn’t break compatibility.

5. **Observability & Security Gates**
   - Ensure metrics/log pipelines capture new fields.
   - Reconfirm secrets/key files have expected permissions and no sensitive data was logged.

### Phase 8.13: Network/API Recovery Protocol (If Something Breaks)

1. **Immediate Assessment**
   ```bash
   cd ~/Documents/qfProjects/quantumNotary
   git status
   pytest tests/smoke --maxfail=1
   curl -d '{"id":1,"jsonrpc":"2.0","method":"system_health","params":[]}' http://localhost:9944
   ```
   - Capture failing logs from both the API and the quantumFusion node.

2. **Recovery Options (ordered preference)**
   - Revert the smallest surface area (specific runtime file, migration, or API module) instead of global resets.
   - Re-run or roll back migrations with `alembic downgrade <rev>` and reseed deterministic fixtures.
   - Restart the local node with the last known-good runtime artifact.
   - As a last resort, branch off (`git checkout -b recovery/quantumnotary-<timestamp>`) before deeper repairs.

3. **Post-Recovery Verification**
   - Repeat the full Phase 0 + Phase 8.12 checks.
   - Document the root cause, fix, and follow-up actions in the relevant story/epic.

### Enforced Agent Compliance Rules

1. **Ledger & API Availability First**: Any change that jeopardizes notarization guarantees, RPC health, or API uptime is automatically blocked until resolved.
2. **Pre-Work Verification**: Specialists must log the result of Phase 0 (node spec version, migration state, smoke tests) before modifying files.
3. **Post-Work Verification**: Work is incomplete until Phase 8.12 succeeds; attach logs or command output summaries to PRs.
4. **State & Artifact Protection**: Never delete runtime artifacts, keystores, Alembic revisions, or API schemas without written instruction.
5. **Coordinated Deployments**: Runtime upgrades, DB migrations, and API releases must remain in a single, BMAD-master-approved rollout plan.

### Quality Assurance Checklist

**✅ Pre-Work Checklist**
- [ ] quantumFusion node reachable (`system_health` succeeds, correct runtime spec).
- [ ] API smoke tests pass locally.
- [ ] SQLAlchemy migrations applied; schema matches head revision.
- [ ] Required secrets/keys available and labeled.
- [ ] Frontend dependencies install cleanly; lint/unit tests pass; design references captured.
- [ ] Story/epic includes target runtime artifact hashes and API contract versions.

**✅ Post-Work Checklist**
- [ ] Full pytest suite (or targeted subset) is green with updated code.
- [ ] Devnet notarization flow succeeds end-to-end.
- [ ] No unapplied migrations or ORM drift.
- [ ] RPC + API observability dashboards show expected signals.
- [ ] UI automation + accessibility checks pass; updated screenshots/video attached.
- [ ] Documentation/story updated with findings, metrics, and deployment notes.

### Emergency Escalation

1. **Document the Failure State**
   ```bash
   cd ~/Documents/qfProjects/quantumNotary
   git status > quantumnotary_failure_report.txt
   pytest tests/smoke --maxfail=1 >> quantumnotary_failure_report.txt 2>&1
   curl -d '{"id":1,"jsonrpc":"2.0","method":"system_health","params":[]}' http://localhost:9944 >> quantumnotary_failure_report.txt 2>&1
   ```
2. **Snapshot Network Context**
   - Record the node logs, block height, runtime spec, and RPC endpoints that failed.
3. **Escalate with Context**
   - Attach the failure report, log excerpts, and reproduction steps when looping in human oversight or external teams.
   - Include recommended mitigation options (rollback, hotfix, or feature toggle).

BMAD Master must halt workstreams if any of these integrity requirements cannot be satisfied and coordinate the appropriate specialists to restore service before continuing development.
6. **Frontend Build Baseline**
   - Install/update frontend dependencies (`npm install`, `pnpm install`, etc.) inside the QuantumNotary repo UI workspace.
   - Run lint + unit tests (`npm run lint`, `npm run test -- --watch=false`) and launch the dev server to verify env vars and API connectivity.
   - Capture current design system references (tokens, Storybook, Figma links) for the story/epic.
