---
layout: default
title: "\"Pull or Not to Pull?'': Investigating Moral Biases in Leading Large Language Models Across Ethical Dilemmas"
---

# "Pull or Not to Pull?'': Investigating Moral Biases in Leading Large Language Models Across Ethical Dilemmas

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07284" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07284v1</a>
  <a href="https://arxiv.org/pdf/2508.07284.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07284v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07284v1', '&quot;Pull or Not to Pull?\'\': Investigating Moral Biases in Leading Large Language Models Across Ethical Dilemmas')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Junchen Ding, Penghao Jiang, Zihao Xu, Ziqi Ding, Yichen Zhu, Jiaojiao Jiang, Yuekang Li

**分类**: cs.CL, cs.AI, cs.CY

**发布日期**: 2025-08-10

---

## 💡 一句话要点

**评估大型语言模型在伦理困境中的道德偏见**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `伦理决策` `大型语言模型` `道德推理` `电车难题` `实证评估` `道德哲学` `模型对齐`

## 📋 核心要点

1. 现有大型语言模型在伦理决策中表现出显著的道德偏见，缺乏一致性和透明度。
2. 本研究通过对14种LLMs进行实证评估，探讨其在多种伦理框架下的道德推理能力。
3. 研究结果显示，增强推理的模型在某些伦理框架下表现出更高的决策果断性，但与人类共识的对齐程度不一。

## 📝 摘要（中文）

随着大型语言模型（LLMs）在伦理敏感决策中的应用日益增加，理解其道德推理过程变得至关重要。本研究对14种领先的LLMs进行了全面的实证评估，涵盖27种不同的电车难题场景，基于包括功利主义、义务论和利他主义在内的十种道德哲学。通过因子提示协议，我们获取了3780个二元决策和自然语言解释，分析了决策的果断性、解释一致性、公共道德对齐和对伦理无关线索的敏感性。研究发现，不同伦理框架和模型类型之间存在显著差异：增强推理的模型表现出更高的果断性和结构化的解释，但并不总是与人类共识更好对齐。值得注意的是，在利他、公平和美德伦理框架下，模型达到了高干预率、低解释冲突和与人类判断最小偏差的“甜蜜区”。然而，在强调亲属关系、合法性或自我利益的框架下，模型常常产生伦理上有争议的结果。这些模式表明，道德提示不仅是行为修正器，还是揭示提供者潜在对齐哲学的诊断工具。我们主张将道德推理作为LLM对齐的主要轴心，并呼吁建立标准化基准，以评估LLMs的决策过程及其原因。

## 🔬 方法详解

**问题定义**：本研究旨在揭示大型语言模型在伦理决策中的道德推理过程及其偏见，现有方法在伦理一致性和透明度方面存在不足。

**核心思路**：通过对14种LLMs在27种电车难题场景下的表现进行系统评估，分析其在不同道德框架下的决策和解释能力，以此揭示模型的道德推理特征。

**技术框架**：研究采用因子提示协议，收集3780个二元决策和自然语言解释，分析维度包括决策果断性、解释一致性等。主要模块包括模型选择、场景设计、数据收集和分析。

**关键创新**：本研究的创新在于系统性地评估了不同道德框架下的LLMs表现，揭示了模型在伦理决策中的潜在偏见和一致性问题，提供了新的评估视角。

**关键设计**：研究中采用了多种道德哲学框架，设计了27个电车难题场景，确保了数据的多样性和代表性，同时分析了模型在不同框架下的决策和解释特征。

## 📊 实验亮点

实验结果显示，增强推理的模型在利他、公平和美德伦理框架下表现出高干预率和低解释冲突，且与人类判断的偏差最小。然而，在强调亲属关系、合法性或自我利益的框架下，模型则表现出伦理上有争议的决策，揭示了道德推理的复杂性。

## 🎯 应用场景

该研究的结果对伦理决策支持系统、自动化法律分析和社会机器人等领域具有重要的应用价值。通过理解和改善大型语言模型的道德推理能力，可以提高其在伦理敏感场景中的决策质量，促进更负责任的人工智能应用。未来，这一研究方向可能推动建立更为标准化的道德评估基准。

## 📄 摘要（原文）

> As large language models (LLMs) increasingly mediate ethically sensitive decisions, understanding their moral reasoning processes becomes imperative. This study presents a comprehensive empirical evaluation of 14 leading LLMs, both reasoning enabled and general purpose, across 27 diverse trolley problem scenarios, framed by ten moral philosophies, including utilitarianism, deontology, and altruism. Using a factorial prompting protocol, we elicited 3,780 binary decisions and natural language justifications, enabling analysis along axes of decisional assertiveness, explanation answer consistency, public moral alignment, and sensitivity to ethically irrelevant cues. Our findings reveal significant variability across ethical frames and model types: reasoning enhanced models demonstrate greater decisiveness and structured justifications, yet do not always align better with human consensus. Notably, "sweet zones" emerge in altruistic, fairness, and virtue ethics framings, where models achieve a balance of high intervention rates, low explanation conflict, and minimal divergence from aggregated human judgments. However, models diverge under frames emphasizing kinship, legality, or self interest, often producing ethically controversial outcomes. These patterns suggest that moral prompting is not only a behavioral modifier but also a diagnostic tool for uncovering latent alignment philosophies across providers. We advocate for moral reasoning to become a primary axis in LLM alignment, calling for standardized benchmarks that evaluate not just what LLMs decide, but how and why.

