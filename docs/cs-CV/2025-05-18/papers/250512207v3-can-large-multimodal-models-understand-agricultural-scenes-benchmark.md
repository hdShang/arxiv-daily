---
layout: default
title: Can Large Multimodal Models Understand Agricultural Scenes? Benchmarking with AgroMind
---

# Can Large Multimodal Models Understand Agricultural Scenes? Benchmarking with AgroMind

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.12207" class="toolbar-btn" target="_blank">📄 arXiv: 2505.12207v3</a>
  <a href="https://arxiv.org/pdf/2505.12207.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.12207v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.12207v3', 'Can Large Multimodal Models Understand Agricultural Scenes? Benchmarking with AgroMind')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Qingmei Li, Yang Zhang, Zurong Mai, Yuhang Chen, Shuohong Lou, Henglian Huang, Jiarui Zhang, Zhiwei Zhang, Yibin Wen, Weijia Li, Haohuan Fu, Jianxi Huang, Juepeng Zheng

**分类**: cs.CV, cs.AI

**发布日期**: 2025-05-18 (更新: 2025-08-13)

**🔗 代码/项目**: [PROJECT_PAGE](https://rssysu.github.io/AgroMind/)

---

## 💡 一句话要点

**提出AgroMind以解决农业遥感基准不足问题**

🎯 **匹配领域**: **支柱三：空间感知与语义 (Perception & Semantics)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `农业遥感` `多模态模型` `基准评估` `空间推理` `作物识别` `环境分析` `数据集整合`

## 📋 核心要点

1. 现有农业遥感基准缺乏多样性和复杂性，无法全面评估大型多模态模型的能力。
2. AgroMind通过整合多种数据集，设计了涵盖多维度任务的综合评估框架，提升了评估的全面性。
3. 实验结果显示，20个开源LMMs和4个闭源模型在多个任务上表现不均，部分LMMs超越了人类表现。

## 📝 摘要（中文）

大型多模态模型（LMMs）在多个领域展现出能力，但农业遥感（RS）领域的综合基准仍然稀缺。现有的农业RS基准存在明显不足，主要体现在数据集场景多样性不足和任务设计过于简化。为此，我们提出AgroMind，一个涵盖空间感知、物体理解、场景理解和场景推理四个任务维度的综合农业遥感基准，共包含13种任务类型，涉及作物识别、健康监测和环境分析等。我们通过整合八个公共数据集和一个私有农田数据集，构建了一个高质量的评估集，包含27,247个问答对和19,615张图像。实验表明，LMMs在空间推理和细粒度识别方面存在显著性能差距，且人类表现落后于多个领先的LMMs。AgroMind为农业RS建立了标准化评估框架，揭示了LMMs在领域知识方面的局限性，并突出了未来工作的关键挑战。

## 🔬 方法详解

**问题定义**：本论文旨在解决农业遥感领域缺乏全面基准的问题。现有方法在场景多样性和任务复杂性上存在明显不足，无法有效评估LMMs的性能。

**核心思路**：我们提出AgroMind，通过整合多个数据集并设计多样化的任务，构建一个全面的评估框架，以更好地测试LMMs在农业遥感中的应用能力。

**技术框架**：整体流程包括数据收集、格式标准化、注释优化和任务定义，最终生成多样化的农业相关问题，并使用LMMs进行推理和响应生成。

**关键创新**：AgroMind的创新在于其综合性和多样性，涵盖了空间感知、物体理解等多个维度，填补了现有基准的空白。

**关键设计**：在数据集构建中，我们整合了八个公共数据集和一个私有数据集，确保了数据的丰富性和多样性，同时设计了13种不同的任务类型以全面评估模型性能。实验中使用了20个开源和4个闭源的LMMs进行比较。

## 📊 实验亮点

实验结果显示，20个开源LMMs和4个闭源模型在AgroMind基准上表现出显著的性能差距，尤其是在空间推理和细粒度识别任务中，部分LMMs的表现超过了人类水平，揭示了当前技术的潜力与局限。

## 🎯 应用场景

AgroMind的研究成果可广泛应用于农业遥感监测、作物健康评估和环境分析等领域。通过提供一个标准化的评估框架，研究者和开发者可以更有效地测试和优化多模态模型在农业场景中的应用，推动农业智能化的发展。

## 📄 摘要（原文）

> Large Multimodal Models (LMMs) has demonstrated capabilities across various domains, but comprehensive benchmarks for agricultural remote sensing (RS) remain scarce. Existing benchmarks designed for agricultural RS scenarios exhibit notable limitations, primarily in terms of insufficient scene diversity in the dataset and oversimplified task design. To bridge this gap, we introduce AgroMind, a comprehensive agricultural remote sensing benchmark covering four task dimensions: spatial perception, object understanding, scene understanding, and scene reasoning, with a total of 13 task types, ranging from crop identification and health monitoring to environmental analysis. We curate a high-quality evaluation set by integrating eight public datasets and one private farmland plot dataset, containing 27,247 QA pairs and 19,615 images. The pipeline begins with multi-source data pre-processing, including collection, format standardization, and annotation refinement. We then generate a diverse set of agriculturally relevant questions through the systematic definition of tasks. Finally, we employ LMMs for inference, generating responses, and performing detailed examinations. We evaluated 20 open-source LMMs and 4 closed-source models on AgroMind. Experiments reveal significant performance gaps, particularly in spatial reasoning and fine-grained recognition, it is notable that human performance lags behind several leading LMMs. By establishing a standardized evaluation framework for agricultural RS, AgroMind reveals the limitations of LMMs in domain knowledge and highlights critical challenges for future work. Data and code can be accessed at https://rssysu.github.io/AgroMind/.

