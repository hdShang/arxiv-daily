---
layout: default
title: Developing Large Language Models for Clinical Research Using One Million Clinical Trials
---

# Developing Large Language Models for Clinical Research Using One Million Clinical Trials

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.16097" class="toolbar-btn" target="_blank">📄 arXiv: 2505.16097</a>
  <a href="https://arxiv.org/pdf/2505.16097.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.16097" onclick="toggleFavorite(this, '2505.16097', 'Developing Large Language Models for Clinical Research Using One Million Clinical Trials')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zifeng Wang, Jiacheng Lin, Qiao Jin, Junyi Gao, Jathurshan Pradeepkumar, Pengcheng Jiang, Zhiyong Lu, Jimeng Sun

**分类**: cs.AI

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**TrialPanorama：构建百万级临床试验数据集，提升LLM在临床研究任务中的性能**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `临床研究` `大型语言模型` `数据集构建` `监督微调` `强化学习` `临床试验` `自然语言处理`

## 📋 核心要点

1. 现有通用LLM在临床推理方面能力有限，难以满足临床研究的特定需求。
2. 论文构建TrialPanorama数据集，并在此基础上微调LLM，以提升其在临床研究任务中的性能。
3. 实验结果表明，基于TrialPanorama训练的8B LLM在多个临床研究任务上显著优于通用LLM。

## 📝 摘要（中文）

本文介绍了一个名为TrialPanorama的大规模结构化资源，它汇集了来自15个全球注册机构的160万条临床试验记录，并将它们与生物医学本体和相关文献联系起来。为了展示其效用，作者构建了一个pipeline，为八个关键临床研究任务构建了15.2万个训练和测试样本。这些任务包括支持系统评价工作流程（研究搜索、研究筛选和证据总结）以及关注试验设计和优化（臂设计、纳入标准设计、终点选择、样本量估计以及试验完成评估和合理化）。对先进大型语言模型（LLM）的基准测试表明，通用LLM在临床推理方面的能力有限。相比之下，作者在TrialPanorama上使用监督微调和强化学习开发的8B LLM在所有八个任务中都优于70B的通用LLM，相对改进分别为73.7%、67.6%、38.4%、37.8%、26.5%、20.7%、20.0%、18.1%和5.2%。TrialPanorama为未来扩展临床研究AI提供了坚实的基础。

## 🔬 方法详解

**问题定义**：现有的大型语言模型在处理临床研究任务时，由于缺乏针对性的训练数据和领域知识，表现出临床推理能力不足的问题。这限制了它们在临床研究中的应用，例如系统评价、试验设计和优化等。

**核心思路**：论文的核心思路是构建一个大规模的、结构化的临床试验数据集TrialPanorama，并利用该数据集对LLM进行微调，使其能够更好地理解和处理临床研究相关的任务。通过监督微调和强化学习，使模型学习到特定领域的知识和推理能力。

**技术框架**：该研究的技术框架主要包括以下几个步骤：1) 数据收集与整合：从15个全球临床试验注册机构收集数据，并进行清洗和整合。2) 数据结构化：将临床试验数据与生物医学本体和相关文献进行链接，构建结构化的TrialPanorama数据集。3) 任务构建：基于TrialPanorama数据集，构建八个关键临床研究任务的训练和测试样本。4) 模型训练与评估：使用监督微调和强化学习在TrialPanorama数据集上训练LLM，并在八个任务上进行评估。

**关键创新**：该研究的关键创新在于构建了TrialPanorama数据集，这是一个大规模的、结构化的临床试验资源，为LLM在临床研究领域的应用提供了数据基础。此外，通过监督微调和强化学习，有效地提升了LLM在临床研究任务中的性能。

**关键设计**：论文中使用了监督微调和强化学习两种方法来训练LLM。监督微调使用标注好的训练数据来调整模型的参数，使其更好地适应特定任务。强化学习则通过奖励机制来引导模型学习，使其能够更好地完成任务。具体参数设置和损失函数等技术细节在论文中未详细说明，属于未知信息。

## 🖼️ 关键图片

<div class="paper-figures">
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.16097/x1.png" alt="fig_0" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.16097/x2.png" alt="fig_1" loading="lazy">
</figure>
<figure class="paper-figure">
<img src="https://arxiv.org/html/2505.16097/x3.png" alt="fig_2" loading="lazy">
</figure>
</div>

## 📊 实验亮点

实验结果表明，基于TrialPanorama数据集训练的8B LLM在八个关键临床研究任务中均优于70B的通用LLM。具体而言，相对改进幅度分别为73.7%、67.6%、38.4%、37.8%、26.5%、20.7%、20.0%、18.1%和5.2%。这些结果表明，针对特定领域的数据集和训练方法能够显著提升LLM在该领域的性能。

## 🎯 应用场景

该研究成果可应用于临床研究的多个领域，例如加速系统评价流程、优化临床试验设计、辅助医生进行决策等。TrialPanorama数据集和训练好的LLM可以作为临床研究人员的有力工具，提高研究效率和质量，并最终改善患者的治疗效果。未来，该方法有望扩展到其他医学领域，推动AI在医疗健康领域的应用。

## 📄 摘要（原文）

> Developing artificial intelligence (AI) for clinical research requires a comprehensive data foundation that supports model training and rigorous evaluation. Here, we introduce TrialPanorama, a large-scale structured resource that aggregates 1.6M clinical trial records from fifteen global registries and links them with biomedical ontologies and associated literature. To demonstrate its utility, we build a pipeline that constructs 152K training and testing samples for eight key clinical research tasks. Three tasks support systematic review workflows, including study search, study screening, and evidence summarization. Five tasks focus on trial design and optimization, including arm design, eligibility criteria design, endpoint selection, sample size estimation, and trial completion assessment and rationalization. Benchmarking cutting-edge large language models (LLMs) reveals that generic LLMs have limited capability in clinical reasoning. In contrast, an 8B LLM we developed on TrialPanorama using supervised finetuning and reinforcement learning wins over the 70B generic counterparts in all eight tasks, with a relative improvement of 73.7%, 67.6%, 38.4%, 37.8%, 26.5%, 20.7%, 20.0%, 18.1%, and 5.2%, respectively. We envision that TrialPanorama provides a solid foundation for future scaling of AI for clinical research.

