---
layout: default
title: Pathology-CoT: Learning Visual Chain-of-Thought Agent from Expert Whole Slide Image Diagnosis Behavior
---

# Pathology-CoT: Learning Visual Chain-of-Thought Agent from Expert Whole Slide Image Diagnosis Behavior

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.04587" target="_blank" class="toolbar-btn">arXiv: 2510.04587v2</a>
    <a href="https://arxiv.org/pdf/2510.04587.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.04587v2" 
            onclick="toggleFavorite(this, '2510.04587v2', 'Pathology-CoT: Learning Visual Chain-of-Thought Agent from Expert Whole Slide Image Diagnosis Behavior')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Sheng Wang, Ruiming Wu, Charles Herndon, Yihang Liu, Shunsuke Koga, Jeanne Shen, Zhi Huang

**分类**: cs.CV

**发布日期**: 2025-10-06 (更新: 2025-10-13)

---

## 💡 一句话要点

**提出Pathology-CoT框架，从专家WSI诊断行为中学习视觉链式推理Agent**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `病理学` `全切片图像` `链式思考` `智能体` `行为学习`

## 📋 核心要点

1. 现有病理学AI系统缺乏模拟专家诊断过程的交互性和可解释性，主要瓶颈在于缺乏专家观察行为的标注数据。
2. Pathology-CoT框架通过AI会话记录器和人机协作，高效构建了包含专家“在哪里看”和“为什么重要”的链式思考数据集。
3. 提出的Pathology-o3智能体在淋巴结转移检测任务中，超越了现有SOTA模型，并在外部验证集中表现出良好的泛化能力。

## 📝 摘要（中文）

诊断全切片图像（WSI）是一个交互式的多阶段过程，包括改变放大倍数和在视野之间移动。尽管最近的病理学基础模型表现出卓越的性能，但仍然缺乏能够决定下一步检查哪个视野、调整放大倍数并提供可解释诊断的实用智能体系统。这种限制主要受限于数据：缺乏对专家观察行为的可扩展、临床对齐的监督，这些行为是隐性的、基于经验的，没有记录在教科书或互联网上，因此也未包含在LLM训练中。本文介绍了一个旨在通过三个关键突破来应对这一挑战的框架。首先，AI会话记录器与标准WSI查看器无缝集成，以不引人注意地记录常规导航，并将查看器日志转换为标准化行为命令和边界框。其次，轻量级的人工参与审查将AI起草的行为命令理由转化为Pathology-CoT数据集，这是一种配对的“在哪里看”和“为什么重要”的形式，与手动构建此类链式思考数据集相比，标签速度提高了六倍。使用这种行为数据，我们构建了Pathology-o3，这是一个两阶段智能体，首先提出重要的ROI，然后执行行为引导的推理。在胃肠道淋巴结转移检测任务中，我们的方法在斯坦福医学的内部验证中实现了100%的召回率，在瑞典的独立外部验证中实现了97.6%的召回率，超过了最先进的OpenAI o3模型，并且可以跨骨干网络泛化。据我们所知，Pathology-CoT是病理学中首批基于行为的智能体系统之一。通过将日常查看器日志转化为可扩展的、经过专家验证的监督，我们的框架使智能病理学成为现实，并为与人类对齐、可升级的临床AI奠定了基础。

## 🔬 方法详解

**问题定义**：论文旨在解决病理学全切片图像（WSI）诊断中，现有AI系统缺乏交互性、可解释性以及无法有效模拟专家诊断流程的问题。现有方法主要依赖于图像级别的标注，忽略了专家在诊断过程中视野移动、放大倍数调整等关键行为，导致模型难以学习专家的诊断策略。

**核心思路**：论文的核心思路是通过记录和学习专家的WSI诊断行为，构建一个能够模拟专家诊断流程的智能体。该智能体不仅能够识别病灶区域，还能像专家一样进行视野导航和放大倍数调整，并给出可解释的诊断理由。这种方法的核心在于将专家的隐性知识显性化，并将其融入到模型的训练过程中。

**技术框架**：Pathology-CoT框架包含三个主要组成部分：AI会话记录器、人机协作标注流程和Pathology-o3智能体。AI会话记录器负责记录专家在使用WSI查看器时的所有操作，包括视野移动、放大倍数调整等。人机协作标注流程利用AI起草行为命令的理由，然后由专家进行审核和修正，从而高效地构建Pathology-CoT数据集。Pathology-o3智能体是一个两阶段模型，首先提出重要的ROI，然后执行行为引导的推理，最终给出诊断结果。

**关键创新**：该论文最重要的技术创新点在于提出了一个从专家行为中学习的框架，通过AI会话记录器和人机协作标注流程，解决了病理学领域缺乏专家行为标注数据的难题。与传统的图像级别标注方法相比，该方法能够更全面地捕捉专家的诊断策略，并将其融入到模型的训练过程中。此外，Pathology-o3智能体通过行为引导的推理，实现了更可解释的诊断结果。

**关键设计**：AI会话记录器需要与现有的WSI查看器无缝集成，以确保记录过程的无侵入性。人机协作标注流程需要设计高效的标注界面和流程，以减少专家的标注负担。Pathology-o3智能体的网络结构和损失函数需要根据具体的任务进行调整，以实现最佳的性能。具体的参数设置和网络结构在论文中可能没有详细描述，属于未知信息。

## 📊 实验亮点

Pathology-o3智能体在胃肠道淋巴结转移检测任务中，在斯坦福医学的内部验证中实现了100%的召回率，在瑞典的独立外部验证中实现了97.6%的召回率，超过了最先进的OpenAI o3模型，并且可以跨骨干网络泛化。这表明该方法具有很强的实用性和泛化能力。

## 🎯 应用场景

该研究成果可应用于病理学辅助诊断、远程病理诊断、病理学教育等领域。通过模拟专家诊断流程，该智能体可以帮助病理医生提高诊断效率和准确性，尤其是在资源匮乏的地区。未来，该技术有望推广到其他医学影像领域，为临床决策提供更可靠的依据。

## 📄 摘要（原文）

> Diagnosing a whole-slide image is an interactive, multi-stage process of changing magnification and moving between fields. Although recent pathology foundation models demonstrated superior performances, practical agentic systems that decide what field to examine next, adjust magnification, and deliver explainable diagnoses are still lacking. Such limitation is largely bottlenecked by data: scalable, clinically aligned supervision of expert viewing behavior that is tacit and experience-based, not documented in textbooks or internet, and therefore absent from LLM training. Here we introduce a framework designed to address this challenge through three key breakthroughs. First, the AI Session Recorder seamlessly integrates with standard whole-slide image viewers to unobtrusively record routine navigation and convert the viewer logs into standardized behavioral commands and bounding boxes. Second, a lightweight human-in-the-loop review turns AI-drafted rationales for behavioral commands into the Pathology-CoT dataset, a form of paired "where to look" and "why it matters", enabling six-fold faster labeling compared to manual constructing such Chain-of-Thought dataset. Using this behavioral data, we build Pathology-o3, a two-stage agent that first proposes important ROIs and then performs behavior-guided reasoning. On the gastrointestinal lymph-node metastasis detection task, our method achieved 100 recall on the internal validation from Stanford Medicine and 97.6 recall on an independent external validation from Sweden, exceeding the state-of-the-art OpenAI o3 model and generalizing across backbones. To our knowledge, Pathology-CoT constitutes one of the first behavior-grounded agentic systems in pathology. Turning everyday viewer logs into scalable, expert-validated supervision, our framework makes agentic pathology practical and establishes a path to human-aligned, upgradeable clinical AI.

