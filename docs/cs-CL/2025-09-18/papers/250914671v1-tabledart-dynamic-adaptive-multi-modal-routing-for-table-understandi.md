---
layout: default
title: "TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding"
---

# TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.14671" class="toolbar-btn" target="_blank">📄 arXiv: 2509.14671v1</a>
  <a href="https://arxiv.org/pdf/2509.14671.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.14671v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.14671v1', 'TableDART: Dynamic Adaptive Multi-Modal Routing for Table Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xiaobo Xing, Wei Yuan, Tong Chen, Quoc Viet Hung Nguyen, Xiangliang Zhang, Hongzhi Yin

**分类**: cs.CL, cs.AI, cs.LG

**发布日期**: 2025-09-18

---

## 💡 一句话要点

**TableDART：提出动态自适应多模态路由框架，用于表格理解。**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `表格理解` `多模态学习` `动态路由` `知识集成` `预训练模型` `自然语言处理` `计算机视觉`

## 📋 核心要点

1. 现有表格理解方法在处理表格数据的语义和结构信息时存在不足，如Table-as-Text丢失结构信息，Table-as-Image语义理解不足。
2. TableDART通过动态选择文本、图像或融合路径，并利用agent进行跨模态知识集成，从而更有效地利用多模态信息。
3. 实验结果表明，TableDART在多个基准测试中取得了新的state-of-the-art性能，显著优于现有开源模型。

## 📝 摘要（中文）

表格数据的语义和结构信息建模是有效表格理解的核心挑战。现有的Table-as-Text方法将表格扁平化以供大型语言模型（LLMs）使用，但丢失了关键的结构线索；Table-as-Image方法保留了结构，但在细粒度语义方面表现不佳。最近的Table-as-Multimodality策略试图结合文本和视觉视图，但它们（1）静态地处理每个查询-表格对的两种模态，不可避免地引入冗余甚至冲突，并且（2）依赖于对MLLM进行昂贵的微调。为此，我们提出了TableDART，一个训练高效的框架，通过重用预训练的单模态模型来集成多模态视图。TableDART引入了一个轻量级的259万参数MLP门控网络，可以为每个表格-查询对动态选择最佳路径（仅文本、仅图像或融合），从而有效地减少来自两种模态的冗余和冲突。此外，我们提出了一个新的agent，通过分析基于文本和图像的模型的输出，来协调跨模态知识集成，可以选择最佳结果或通过推理合成新的答案。这种设计避免了完全MLLM微调的过高成本。在七个基准测试上的大量实验表明，TableDART在开源模型中建立了新的最先进性能，平均超过最强的基线4.02%。

## 🔬 方法详解

**问题定义**：论文旨在解决表格理解任务中，如何有效融合表格的文本和图像信息的问题。现有方法要么损失结构信息（Table-as-Text），要么难以捕捉细粒度语义（Table-as-Image），而多模态方法又存在计算冗余和需要大量微调的问题。

**核心思路**：论文的核心思路是动态地、自适应地选择最适合当前表格-查询对的模态路径（文本、图像或融合），并利用一个agent来协调跨模态知识的集成。这种方法旨在减少冗余计算，避免模态冲突，并降低对大型多模态模型进行昂贵微调的需求。

**技术框架**：TableDART框架包含以下主要模块：1) 文本编码器：使用预训练的语言模型编码表格文本；2) 图像编码器：使用预训练的视觉模型编码表格图像；3) 门控网络：一个轻量级的MLP，根据表格-查询对的特征动态选择最佳模态路径；4) 跨模态知识集成Agent：分析文本和图像模型的输出，选择最佳结果或合成新的答案。

**关键创新**：TableDART的关键创新在于其动态自适应的多模态路由机制和跨模态知识集成Agent。动态路由允许模型根据输入自适应地选择最合适的模态，避免了静态处理所有模态的冗余和冲突。跨模态知识集成Agent则能够有效地整合来自不同模态的信息，提升最终的预测准确性。

**关键设计**：门控网络是一个2.59M参数的MLP，输入是表格和查询的特征向量，输出是选择不同模态路径的概率。跨模态知识集成Agent使用强化学习进行训练，目标是最大化预测准确率。损失函数包括交叉熵损失和强化学习奖励。

## 📊 实验亮点

TableDART在七个基准测试中取得了新的state-of-the-art性能，平均超过最强的基线4.02%。 实验结果表明，TableDART能够有效地融合表格的文本和图像信息，并显著提升表格理解的准确性。 此外，TableDART的训练效率高，避免了对大型多模态模型进行昂贵的微调。

## 🎯 应用场景

TableDART可应用于各种需要理解表格数据的场景，例如智能问答、数据分析、报告生成等。该研究成果有助于提升机器对表格数据的理解能力，从而在金融、医疗、教育等领域实现更智能化的应用。未来，该方法可以进一步扩展到处理更复杂的表格结构和更多模态的数据。

## 📄 摘要（原文）

> Modeling semantic and structural information from tabular data remains a core challenge for effective table understanding. Existing Table-as-Text approaches flatten tables for large language models (LLMs), but lose crucial structural cues, while Table-as-Image methods preserve structure yet struggle with fine-grained semantics. Recent Table-as-Multimodality strategies attempt to combine textual and visual views, but they (1) statically process both modalities for every query-table pair within a large multimodal LLMs (MLLMs), inevitably introducing redundancy and even conflicts, and (2) depend on costly fine-tuning of MLLMs. In light of this, we propose TableDART, a training-efficient framework that integrates multimodal views by reusing pretrained single-modality models. TableDART introduces a lightweight 2.59M-parameter MLP gating network that dynamically selects the optimal path (either Text-only, Image-only, or Fusion) for each table-query pair, effectively reducing redundancy and conflicts from both modalities. In addition, we propose a novel agent to mediate cross-modal knowledge integration by analyzing outputs from text- and image-based models, either selecting the best result or synthesizing a new answer through reasoning. This design avoids the prohibitive costs of full MLLM fine-tuning. Extensive experiments on seven benchmarks show that TableDART establishes new state-of-the-art performance among open-source models, surpassing the strongest baseline by an average of 4.02%. The code is available at: https://anonymous.4open.science/r/TableDART-C52B

