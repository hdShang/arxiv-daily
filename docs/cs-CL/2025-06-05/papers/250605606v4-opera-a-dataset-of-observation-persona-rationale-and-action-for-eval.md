---
layout: default
title: "OPeRA: A Dataset of Observation, Persona, Rationale, and Action for Evaluating LLMs on Human Online Shopping Behavior Simulation"
---

# OPeRA: A Dataset of Observation, Persona, Rationale, and Action for Evaluating LLMs on Human Online Shopping Behavior Simulation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05606" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05606v4</a>
  <a href="https://arxiv.org/pdf/2506.05606.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05606v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05606v4', 'OPeRA: A Dataset of Observation, Persona, Rationale, and Action for Evaluating LLMs on Human Online Shopping Behavior Simulation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ziyi Wang, Yuxuan Lu, Wenbo Li, Amirali Amini, Bo Sun, Yakov Bart, Weimin Lyu, Jiri Gesi, Tian Wang, Jing Huang, Yu Su, Upol Ehsan, Malihe Alikhani, Toby Jia-Jun Li, Lydia Chilton, Dakuo Wang

**分类**: cs.CL, cs.HC

**发布日期**: 2025-06-05 (更新: 2025-07-24)

---

## 💡 一句话要点

**提出OPeRA数据集以解决LLMs模拟用户在线购物行为的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `用户行为模拟` `在线购物` `数据集构建` `个性化推荐` `人机交互`

## 📋 核心要点

1. 现有方法在模拟用户在线购物行为时缺乏高质量的数据集，难以评估LLMs的真实表现。
2. 本文提出OPeRA数据集，全面捕捉用户的角色、行为观察和推理过程，提供高保真度的数据收集工具。
3. 通过OPeRA，建立了评估LLMs预测用户行为的基准，为个性化数字双胞胎的研究奠定基础。

## 📝 摘要（中文）

大型语言模型（LLMs）能否准确模拟特定用户的下一步网络行为？尽管LLMs在生成“可信”的人类行为方面表现出色，但评估其模仿真实用户行为的能力仍然是一个开放性挑战，主要是由于缺乏高质量、公开可用的数据集来捕捉用户的可观察行为和内部推理。为了解决这一问题，本文提出了OPeRA，一个从真实人类参与者的在线购物会话中收集的观察、角色、推理和行动的新数据集。OPeRA是第一个全面捕捉用户角色、浏览观察、细粒度网络行为和即时自我报告推理的公共数据集。通过OPeRA，我们建立了第一个基准，以评估当前LLMs在给定角色和<观察、行动、推理>历史的情况下，预测特定用户下一步行动和推理的能力。

## 🔬 方法详解

**问题定义**：本文旨在解决大型语言模型在模拟用户在线购物行为时的评估难题。现有方法缺乏能够捕捉用户行为和内在推理的高质量数据集，导致评估结果不准确。

**核心思路**：论文提出了OPeRA数据集，旨在通过真实用户的在线购物会话，收集用户的角色、行为观察、推理和行动数据，以提高LLMs在模拟用户行为方面的准确性。

**技术框架**：OPeRA数据集的构建包括两个主要模块：在线问卷和自定义浏览器插件。在线问卷用于收集用户角色信息，而浏览器插件则实时记录用户的行为和推理。

**关键创新**：OPeRA是第一个全面捕捉用户行为和推理的公共数据集，填补了现有数据集在这一领域的空白，使得LLMs的评估更加真实和可靠。

**关键设计**：数据收集过程中，采用了高保真度的问卷设计和浏览器插件，确保了数据的准确性和丰富性。数据集包含用户的角色信息、浏览行为和即时推理，提供了丰富的上下文信息。

## 📊 实验亮点

通过使用OPeRA数据集，研究者首次建立了评估LLMs预测用户行为的基准，结果表明，当前的LLMs在预测特定用户的下一步行动和推理方面具有一定的能力，但仍有提升空间。具体性能数据和对比基线尚未披露，未来研究将进一步探索这些模型的改进方向。

## 🎯 应用场景

OPeRA数据集的潜在应用领域包括个性化推荐系统、智能客服和虚拟购物助手等。通过更准确地模拟用户行为，LLMs可以在这些应用中提供更具个性化的服务，提升用户体验。未来，该数据集还可能推动个性化数字双胞胎的研究，促进人机交互的进一步发展。

## 📄 摘要（原文）

> Can large language models (LLMs) accurately simulate the next web action of a specific user? While LLMs have shown promising capabilities in generating ``believable'' human behaviors, evaluating their ability to mimic real user behaviors remains an open challenge, largely due to the lack of high-quality, publicly available datasets that capture both the observable actions and the internal reasoning of an actual human user. To address this gap, we introduce OPERA, a novel dataset of Observation, Persona, Rationale, and Action collected from real human participants during online shopping sessions. OPERA is the first public dataset that comprehensively captures: user personas, browser observations, fine-grained web actions, and self-reported just-in-time rationales. We developed both an online questionnaire and a custom browser plugin to gather this dataset with high fidelity. Using OPERA, we establish the first benchmark to evaluate how well current LLMs can predict a specific user's next action and rationale with a given persona and <observation, action, rationale> history. This dataset lays the groundwork for future research into LLM agents that aim to act as personalized digital twins for human.

