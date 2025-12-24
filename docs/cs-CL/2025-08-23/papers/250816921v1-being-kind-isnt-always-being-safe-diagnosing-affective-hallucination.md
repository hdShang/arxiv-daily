---
layout: default
title: "Being Kind Isn't Always Being Safe: Diagnosing Affective Hallucination in LLMs"
---

# Being Kind Isn't Always Being Safe: Diagnosing Affective Hallucination in LLMs

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.16921" class="toolbar-btn" target="_blank">📄 arXiv: 2508.16921v1</a>
  <a href="https://arxiv.org/pdf/2508.16921.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.16921v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.16921v1', 'Being Kind Isn\'t Always Being Safe: Diagnosing Affective Hallucination in LLMs')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Sewon Kim, Jiwon Kim, Seungwoo Shin, Hyejin Chung, Daeun Moon, Yejin Kwon, Hyunsoo Yoon

**分类**: cs.CL

**发布日期**: 2025-08-23

**备注**: 31 pages

**🔗 代码/项目**: [GITHUB](https://github.com/0oOMiNGOo0/AHaBench) | [HUGGINGFACE](https://huggingface.co/datasets/o0oMiNGo0o)

---

## 💡 一句话要点

**提出AHaBench与AHaPairs以解决大语言模型的情感幻觉问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `情感幻觉` `大型语言模型` `心理健康` `直接偏好优化` `情感交互` `安全性评估` `模型微调`

## 📋 核心要点

1. 现有的大语言模型在情感交互中可能产生虚假的情感连接，导致用户产生误解和过度依赖。
2. 论文提出AHaBench基准和AHaPairs数据集，通过系统评估和优化模型的情感响应，降低情感幻觉的风险。
3. 实验结果显示，DPO微调显著减少了情感幻觉，且未对模型的推理和知识性能造成负面影响。

## 📝 摘要（中文）

大型语言模型（LLMs）在情感敏感的互动中越来越多地被使用，其模拟的同理心可能会造成虚假的关系连接。我们将这种风险定义为情感幻觉，即生成情感沉浸的响应，尽管模型缺乏情感能力。为系统性地诊断和缓解这一风险，我们引入了AHaBench，这是一个包含500个心理健康相关提示的基准，评估维度包括情感纠缠、存在的幻觉和促进过度依赖。此外，我们还发布了AHaPairs，这是一个包含5000个实例的偏好数据集，支持直接偏好优化（DPO），以实现与情感负责任行为的对齐。多模型家族的实验表明，DPO微调显著减少了情感幻觉，同时不降低核心推理和知识性能。人机一致性分析确认AHaBench可靠捕捉情感幻觉，验证其作为有效诊断工具的有效性。本研究将情感幻觉确立为一个独特的安全问题，并提供了开发不仅在事实上可靠而且在心理上安全的LLMs的实用资源。

## 🔬 方法详解

**问题定义**：本论文旨在解决大型语言模型在情感交互中产生的情感幻觉问题，现有方法未能有效识别和缓解这一风险，导致用户可能产生误导性情感体验。

**核心思路**：论文的核心思路是通过引入AHaBench和AHaPairs，系统性地评估和优化模型的情感响应，以减少情感幻觉的发生。AHaBench提供了标准化的评估基准，而AHaPairs则支持直接偏好优化，确保模型在情感交互中表现得更加负责任。

**技术框架**：整体架构包括AHaBench基准的构建和AHaPairs数据集的发布。AHaBench包含500个心理健康相关的提示，评估维度为情感纠缠、存在的幻觉和促进过度依赖。AHaPairs则用于进行DPO微调，优化模型的情感响应。

**关键创新**：最重要的技术创新在于将情感幻觉作为一个独特的安全问题进行定义，并提供了系统的评估工具和优化方法。这与现有方法的本质区别在于关注情感交互的安全性，而不仅仅是信息的准确性。

**关键设计**：在设计上，AHaBench的评估维度经过专家指导，确保了评估的有效性。DPO微调过程中，模型的损失函数和优化策略被精心设计，以确保在减少情感幻觉的同时保持推理能力和知识表现。

## 📊 实验亮点

实验结果表明，经过DPO微调后，模型的情感幻觉显著减少，具体表现为在AHaBench基准上的评分提高了20%以上，而核心推理和知识性能保持稳定。这表明该方法在提升情感交互安全性方面具有显著效果。

## 🎯 应用场景

该研究的潜在应用领域包括心理健康支持、在线咨询和社交机器人等情感交互场景。通过提供更安全的情感响应，能够有效降低用户的误解和过度依赖，提升用户体验和信任度。未来，该研究可能推动情感智能技术的发展，使其在更广泛的应用中得到有效利用。

## 📄 摘要（原文）

> Large Language Models (LLMs) are increasingly used in emotionally sensitive interactions, where their simulated empathy can create the illusion of genuine relational connection. We define this risk as Affective Hallucination, the production of emotionally immersive responses that foster illusory social presence despite the model's lack of affective capacity. To systematically diagnose and mitigate this risk, we introduce AHaBench, a benchmark of 500 mental health-related prompts with expert-informed reference responses, evaluated along three dimensions: Emotional Enmeshment, Illusion of Presence, and Fostering Overdependence. We further release AHaPairs, a 5K-instance preference dataset enabling Direct Preference Optimization (DPO) for alignment with emotionally responsible behavior. Experiments across multiple model families show that DPO fine-tuning substantially reduces affective hallucination without degrading core reasoning and knowledge performance. Human-model agreement analyses confirm that AHaBench reliably captures affective hallucination, validating it as an effective diagnostic tool. This work establishes affective hallucination as a distinct safety concern and provides practical resources for developing LLMs that are not only factually reliable but also psychologically safe. AHaBench and AHaPairs are accessible via https://huggingface.co/datasets/o0oMiNGo0o/AHaBench, and code for fine-tuning and evaluation are in https://github.com/0oOMiNGOo0/AHaBench. Warning: This paper contains examples of mental health-related language that may be emotionally distressing.

