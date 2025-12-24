---
layout: default
title: "Embodied Arena: A Comprehensive, Unified, and Evolving Evaluation Platform for Embodied AI"
---

# Embodied Arena: A Comprehensive, Unified, and Evolving Evaluation Platform for Embodied AI

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15273" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15273v2</a>
  <a href="https://arxiv.org/pdf/2509.15273.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15273v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15273v2', 'Embodied Arena: A Comprehensive, Unified, and Evolving Evaluation Platform for Embodied AI')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fei Ni, Min Zhang, Pengyi Li, Yifu Yuan, Lingfeng Zhang, Yuecheng Liu, Peilong Han, Longxin Kou, Shaojin Ma, Jinbin Qiao, David Gamaliel Arcos Bravo, Yuening Wang, Xiao Hu, Zhanguang Zhang, Xianze Yao, Yutong Li, Zhao Zhang, Ying Wen, Ying-Cong Chen, Xiaodan Liang, Liang Lin, Bin He, Haitham Bou-Ammar, He Wang, Huazhe Xu, Jiankang Deng, Shan Luo, Shuqiang Jiang, Wei Pan, Yang Gao, Stefanos Zafeiriou, Jan Peters, Yuzheng Zhuang, Yingxue Zhang, Yan Zheng, Hongyao Tang, Jianye Hao

**分类**: cs.RO

**发布日期**: 2025-09-18 (更新: 2025-09-23)

**备注**: 32 pages, 5 figures, Embodied Arena Technical Report

---

## 💡 一句话要点

**Embodied Arena：构建全面、统一、可演进的具身智能评估平台**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `具身智能` `评估平台` `机器人` `自动化数据生成` `能力分类` `基准测试` `大型语言模型`

## 📋 核心要点

1. 具身智能发展受限于缺乏系统性能力理解、统一评估标准和可扩展数据获取方法。
2. Embodied Arena平台通过构建能力分类、统一评估系统和自动化数据生成管道来解决这些问题。
3. 该平台发布实时排行榜，提供模型能力的全面概述，并总结了九个关键发现，以推动领域进步。

## 📝 摘要（中文）

具身智能的发展显著落后于大型基础模型，这归因于三个关键挑战：(1) 缺乏对具身智能所需核心能力的系统性理解，导致研究缺乏明确目标；(2) 缺乏统一和标准化的评估系统，使得跨基准评估不可行；(3) 用于具身数据的自动化和可扩展获取方法不发达，为模型扩展造成了关键瓶颈。为了解决这些障碍，我们提出了Embodied Arena，这是一个全面、统一和不断发展的具身智能评估平台。我们的平台建立了一个系统的具身能力分类法，涵盖三个层次（感知、推理、任务执行）、七个核心能力和25个细粒度维度，从而实现具有系统研究目标的统一评估。我们引入了一个建立在统一基础设施之上的标准化评估系统，该系统支持跨三个领域（2D/3D具身问答、导航、任务规划）的22个不同基准和来自20多个全球机构的30多个高级模型的灵活集成。此外，我们开发了一种新颖的LLM驱动的自动化生成管道，确保可扩展的具身评估数据，并不断发展以实现多样性和全面性。Embodied Arena发布了三个实时排行榜（具身问答、导航、任务规划），具有双重视角（基准视图和能力视图），提供了高级模型能力的全面概述。特别是，我们总结了从Embodied Arena排行榜的评估结果中得出的九个发现。这有助于建立明确的研究方向并查明关键的研究问题，从而推动具身智能领域的进步。

## 🔬 方法详解

**问题定义**：具身智能领域面临缺乏系统性评估标准和可扩展数据的问题，导致研究方向不明确，模型性能难以有效提升。现有方法往往针对特定任务或环境设计，缺乏通用性和可比性。

**核心思路**：Embodied Arena的核心在于构建一个全面、统一和可演进的评估平台，通过系统性的能力分类、标准化的评估流程和自动化数据生成，为具身智能研究提供清晰的目标和可衡量的指标。平台旨在促进不同模型和算法之间的公平比较，并推动领域内的持续进步。

**技术框架**：Embodied Arena平台包含三个主要组成部分：(1) **能力分类体系**：将具身智能能力划分为感知、推理和任务执行三个层次，并进一步细分为七个核心能力和25个细粒度维度。(2) **统一评估系统**：构建在统一的基础设施之上，支持集成来自不同领域的22个基准测试，涵盖2D/3D具身问答、导航和任务规划等任务。(3) **自动化数据生成管道**：利用大型语言模型（LLM）驱动的自动化生成流程，实现可扩展的具身评估数据生成，并保证数据的多样性和全面性。

**关键创新**：Embodied Arena的关键创新在于其全面性和统一性。它不仅提供了一个标准化的评估平台，还构建了一个系统的能力分类体系，使得研究人员可以更清晰地了解模型的优势和不足。此外，LLM驱动的自动化数据生成管道解决了具身智能领域数据稀缺的问题，为模型训练和评估提供了充足的资源。

**关键设计**：平台采用模块化设计，方便集成新的基准测试和模型。能力分类体系的设计参考了认知科学和机器人学的相关理论，力求全面和准确地反映具身智能的核心能力。自动化数据生成管道利用LLM生成多样化的场景和任务描述，并通过人工验证保证数据的质量。

## 📊 实验亮点

Embodied Arena平台集成了22个基准测试和30多个高级模型，并发布了三个实时排行榜。通过对排行榜数据的分析，论文总结了九个关键发现，例如，现有模型在复杂环境下的导航能力仍然有限，以及在多模态推理方面存在不足。这些发现为未来的研究方向提供了重要的参考。

## 🎯 应用场景

Embodied Arena可应用于机器人导航、智能家居、自动驾驶等领域。通过该平台，研究人员可以系统地评估和提升具身智能模型的性能，从而开发出更智能、更可靠的机器人系统，更好地服务于人类生活。

## 📄 摘要（原文）

> Embodied AI development significantly lags behind large foundation models due to three critical challenges: (1) lack of systematic understanding of core capabilities needed for Embodied AI, making research lack clear objectives; (2) absence of unified and standardized evaluation systems, rendering cross-benchmark evaluation infeasible; and (3) underdeveloped automated and scalable acquisition methods for embodied data, creating critical bottlenecks for model scaling. To address these obstacles, we present Embodied Arena, a comprehensive, unified, and evolving evaluation platform for Embodied AI. Our platform establishes a systematic embodied capability taxonomy spanning three levels (perception, reasoning, task execution), seven core capabilities, and 25 fine-grained dimensions, enabling unified evaluation with systematic research objectives. We introduce a standardized evaluation system built upon unified infrastructure supporting flexible integration of 22 diverse benchmarks across three domains (2D/3D Embodied Q&A, Navigation, Task Planning) and 30+ advanced models from 20+ worldwide institutes. Additionally, we develop a novel LLM-driven automated generation pipeline ensuring scalable embodied evaluation data with continuous evolution for diversity and comprehensiveness. Embodied Arena publishes three real-time leaderboards (Embodied Q&A, Navigation, Task Planning) with dual perspectives (benchmark view and capability view), providing comprehensive overviews of advanced model capabilities. Especially, we present nine findings summarized from the evaluation results on the leaderboards of Embodied Arena. This helps to establish clear research veins and pinpoint critical research problems, thereby driving forward progress in the field of Embodied AI.

