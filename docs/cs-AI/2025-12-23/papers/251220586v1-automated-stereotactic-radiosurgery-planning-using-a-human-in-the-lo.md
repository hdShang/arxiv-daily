---
layout: default
title: Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent
---

# Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.20586" class="toolbar-btn" target="_blank">📄 arXiv: 2512.20586v1</a>
  <a href="https://arxiv.org/pdf/2512.20586.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.20586v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2512.20586v1', 'Automated stereotactic radiosurgery planning using a human-in-the-loop reasoning large language model agent')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Humza Nusrat, Luke Francisco, Bing Luo, Hassan Bagher-Ebadian, Joshua Kim, Karen Chin-Snyder, Salim Siddiqui, Mira Shah, Eric Mellon, Mohammad Ghassemi, Anthony Doemer, Benjamin Movsas, Kundan Thind

**分类**: cs.AI, cs.CL, cs.HC

**发布日期**: 2025-12-23

---

## 💡 一句话要点

**SAGE：基于人机协同推理的大语言模型自动立体定向放射外科计划系统**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `立体定向放射外科` `大语言模型` `思维链推理` `自动化计划` `剂量计划` `人机协同` `透明AI`

## 📋 核心要点

1. 传统SRS计划制定依赖人工，耗时且易受经验影响，黑盒AI方法缺乏透明度，难以临床信任。
2. SAGE利用大语言模型的推理能力，模拟人类专家进行剂量计划制定，提升透明度和可控性。
3. 实验表明，SAGE在剂量学指标上与人类专家相当，并能有效降低耳蜗剂量，同时提供可审计的决策过程。

## 📝 摘要（中文）

立体定向放射外科(SRS)需要在关键结构周围进行精确的剂量塑形，但黑盒AI系统由于透明度问题，临床应用受限。本文测试了思维链推理是否能改进智能体规划。研究回顾性分析了41例接受18Gy单次SRS治疗的脑转移患者。开发了SAGE（用于生成剂量专业知识的安全智能体），这是一个基于LLM的规划智能体，用于自动SRS治疗计划。两种变体为每个病例生成计划：一种使用非推理模型，另一种使用推理模型。推理变体在主要终点（PTV覆盖率、最大剂量、适形指数、梯度指数；所有p > 0.21）上显示出与人类计划员相当的计划剂量学，同时将耳蜗剂量降低到人类基线以下（p = 0.022）。当被提示改进适形性时，推理模型表现出系统的规划行为，包括前瞻性约束验证（457个实例）和权衡考虑（609个实例），而标准模型没有表现出这些审议过程（分别为0和7个实例）。内容分析表明，约束验证和因果解释集中在推理智能体中。优化轨迹可作为可审计的日志，为透明的自动化规划提供了一条途径。

## 🔬 方法详解

**问题定义**：立体定向放射外科(SRS)治疗计划的制定需要精确的剂量控制，以确保肿瘤区域得到充分照射，同时保护周围的关键器官。现有的AI方法，尤其是黑盒模型，虽然可能在性能上有所提升，但缺乏透明度和可解释性，导致临床医生难以信任和应用。因此，需要一种既能自动化计划制定，又能提供清晰决策过程的智能系统。

**核心思路**：本文的核心思路是利用大语言模型(LLM)的推理能力，模拟人类专家在SRS计划制定过程中的思考方式。通过思维链(Chain-of-Thought)推理，LLM可以逐步分析问题、验证约束条件、权衡不同方案，并最终生成治疗计划。这种方法旨在提高计划制定的透明度和可控性，从而增强临床医生的信任。

**技术框架**：SAGE (Secure Agent for Generative Dose Expertise) 系统的整体架构包含以下几个主要模块：1) LLM推理引擎：负责执行思维链推理，生成计划步骤和决策；2) 剂量计算模块：根据LLM生成的计划，计算剂量分布；3) 约束验证模块：检查计划是否满足预设的剂量约束条件；4) 优化模块：根据约束验证结果，调整计划参数，迭代优化剂量分布；5) 日志记录模块：记录LLM的推理过程和优化轨迹，提供可审计的决策过程。

**关键创新**：该论文最重要的技术创新点在于将大语言模型的推理能力引入到SRS治疗计划制定中。与传统的黑盒AI方法不同，SAGE能够提供清晰的决策过程，包括约束验证和权衡考虑。这种透明性使得临床医生能够理解和信任AI生成的计划，从而促进AI在临床实践中的应用。此外，SAGE还通过可审计的日志记录，为计划的验证和改进提供了依据。

**关键设计**：SAGE的关键设计包括：1) 使用思维链提示(Chain-of-Thought prompting)来引导LLM进行推理；2) 设计了专门的约束验证和权衡考虑模块，以确保计划的质量和安全性；3) 采用了迭代优化策略，逐步改进剂量分布；4) 实现了详细的日志记录，包括LLM的推理过程和优化轨迹。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20586v1/FIG1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20586v1/FIG2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2512.20586v1/FIG3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

SAGE在主要剂量学指标（PTV覆盖率、最大剂量、适形指数、梯度指数）上与人类计划员相当(p>0.21)，同时显著降低了耳蜗剂量(p=0.022)。在改进适形性方面，推理模型展示了457个约束验证实例和609个权衡考虑实例，而标准模型几乎没有这些行为（0和7个实例）。这些结果表明，SAGE的推理能力能够有效提高计划质量和透明度。

## 🎯 应用场景

该研究成果可应用于自动化放射治疗计划制定，提高计划效率和质量，降低对人工经验的依赖。潜在应用领域包括脑转移瘤、三叉神经痛等需要精确剂量控制的疾病治疗。未来可扩展到其他类型的放射治疗，并与其他临床信息系统集成，实现更智能化的治疗决策。

## 📄 摘要（原文）

> Stereotactic radiosurgery (SRS) demands precise dose shaping around critical structures, yet black-box AI systems have limited clinical adoption due to opacity concerns. We tested whether chain-of-thought reasoning improves agentic planning in a retrospective cohort of 41 patients with brain metastases treated with 18 Gy single-fraction SRS. We developed SAGE (Secure Agent for Generative Dose Expertise), an LLM-based planning agent for automated SRS treatment planning. Two variants generated plans for each case: one using a non-reasoning model, one using a reasoning model. The reasoning variant showed comparable plan dosimetry relative to human planners on primary endpoints (PTV coverage, maximum dose, conformity index, gradient index; all p > 0.21) while reducing cochlear dose below human baselines (p = 0.022). When prompted to improve conformity, the reasoning model demonstrated systematic planning behaviors including prospective constraint verification (457 instances) and trade-off deliberation (609 instances), while the standard model exhibited none of these deliberative processes (0 and 7 instances, respectively). Content analysis revealed that constraint verification and causal explanation concentrated in the reasoning agent. The optimization traces serve as auditable logs, offering a path toward transparent automated planning.

