---
layout: default
title: "SCOPE: Speech-guided COllaborative PErception Framework for Surgical Scene Segmentation"
---

# SCOPE: Speech-guided COllaborative PErception Framework for Surgical Scene Segmentation

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.10748" class="toolbar-btn" target="_blank">📄 arXiv: 2509.10748v1</a>
  <a href="https://arxiv.org/pdf/2509.10748.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.10748v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.10748v1', 'SCOPE: Speech-guided COllaborative PErception Framework for Surgical Scene Segmentation')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jecia Z. Y. Mao, Francis X Creighton, Russell H Taylor, Manish Sahu

**分类**: cs.CV

**发布日期**: 2025-09-12

---

## 💡 一句话要点

**SCOPE框架：语音引导的协同感知，用于手术场景分割**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `手术场景分割` `语音引导` `协同感知` `视觉基础模型` `大型语言模型` `人机协作` `术中辅助`

## 📋 核心要点

1. 现有手术场景分割方法依赖领域特定数据和标注，难以适应新场景和类别。
2. SCOPE框架结合LLM推理和VFM感知，通过语音引导实现手术器械的即时分割和跟踪。
3. 在Cataract1k和颅底数据集上的实验以及模拟实验验证了SCOPE框架的潜力。

## 📝 摘要（中文）

精确分割和跟踪手术场景中的相关元素对于实现上下文感知的术中辅助和决策至关重要。目前的解决方案依赖于特定领域的监督模型，这些模型依赖于标记数据，并且需要特定领域的数据来适应新的手术场景和超出预定义标签类别。提示驱动的视觉基础模型（VFM）的最新进展已经实现了跨异构医学图像的开放集、零样本分割。然而，这些模型对人工视觉或文本提示的依赖限制了它们在术中手术环境中的部署。我们引入了一种语音引导的协同感知（SCOPE）框架，该框架集成了大型语言模型（LLM）的推理能力与开放集VFM的感知能力，以支持术中视频流中手术器械和解剖结构的即时分割、标记和跟踪。该框架的一个关键组件是协同感知代理，它生成VFM生成的分割的顶级候选对象，并结合来自临床医生的直观语音反馈，以引导手术器械的分割，从而形成自然的人机协作模式。之后，器械本身充当交互式指针，以标记手术场景的其他元素。我们在公开的Cataract1k数据集的一个子集和一个内部的离体颅底数据集上评估了我们提出的框架，以证明其生成手术场景的即时分割和跟踪的潜力。此外，我们通过现场模拟离体实验展示了其动态能力。这种人机协作模式展示了开发适应性强、免提、以外科医生为中心的动态手术室环境工具的潜力。

## 🔬 方法详解

**问题定义**：现有手术场景分割方法依赖于大量标注数据和特定领域的知识，难以泛化到新的手术场景和未知的物体类别。此外，依赖人工视觉或文本提示的方式在术中手术环境中不实用。

**核心思路**：利用大型语言模型（LLM）的推理能力和视觉基础模型（VFM）的感知能力，通过语音引导实现手术场景的即时分割和跟踪。核心思想是将医生的语音指令作为指导信号，驱动VFM进行分割，并利用分割结果反过来辅助医生进行更精确的标注。

**技术框架**：SCOPE框架包含以下主要模块：1) 语音识别模块：将医生的语音指令转换为文本；2) LLM推理模块：根据语音指令生成VFM的分割提示；3) VFM分割模块：根据LLM生成的提示，对视频帧进行分割；4) 协同感知代理：选择最佳分割候选，并允许医生通过语音进行修正；5) 跟踪模块：对分割后的物体进行跟踪。

**关键创新**：该框架的关键创新在于将语音作为VFM的引导信号，实现了人机协同的分割和标注。与传统的依赖人工视觉或文本提示的方法相比，SCOPE框架更加自然和高效。此外，该框架利用手术器械作为交互式指针，进一步扩展了标注范围。

**关键设计**：协同感知代理是关键设计之一，它负责从VFM生成的多个分割候选中选择最佳结果，并允许医生通过语音进行修正。具体的选择策略和修正机制未知，但推测可能涉及置信度评分、视觉一致性以及语音指令的语义分析。

## 📊 实验亮点

论文在Cataract1k数据集和内部颅底数据集上进行了评估，并进行了模拟的离体实验。实验结果表明，SCOPE框架能够生成手术场景的即时分割和跟踪。具体的性能指标和对比基线未知，但模拟实验展示了该框架在动态手术环境中的潜力。

## 🎯 应用场景

SCOPE框架可应用于术中导航、手术机器人辅助、远程手术等领域。通过提供实时、精确的手术场景分割和跟踪，可以帮助医生更好地理解手术过程，提高手术效率和安全性。未来，该框架有望成为智能手术室的重要组成部分，实现更加智能化和个性化的手术辅助。

## 📄 摘要（原文）

> Accurate segmentation and tracking of relevant elements of the surgical scene is crucial to enable context-aware intraoperative assistance and decision making. Current solutions remain tethered to domain-specific, supervised models that rely on labeled data and required domain-specific data to adapt to new surgical scenarios and beyond predefined label categories. Recent advances in prompt-driven vision foundation models (VFM) have enabled open-set, zero-shot segmentation across heterogeneous medical images. However, dependence of these models on manual visual or textual cues restricts their deployment in introperative surgical settings. We introduce a speech-guided collaborative perception (SCOPE) framework that integrates reasoning capabilities of large language model (LLM) with perception capabilities of open-set VFMs to support on-the-fly segmentation, labeling and tracking of surgical instruments and anatomy in intraoperative video streams. A key component of this framework is a collaborative perception agent, which generates top candidates of VFM-generated segmentation and incorporates intuitive speech feedback from clinicians to guide the segmentation of surgical instruments in a natural human-machine collaboration paradigm. Afterwards, instruments themselves serve as interactive pointers to label additional elements of the surgical scene. We evaluated our proposed framework on a subset of publicly available Cataract1k dataset and an in-house ex-vivo skull-base dataset to demonstrate its potential to generate on-the-fly segmentation and tracking of surgical scene. Furthermore, we demonstrate its dynamic capabilities through a live mock ex-vivo experiment. This human-AI collaboration paradigm showcase the potential of developing adaptable, hands-free, surgeon-centric tools for dynamic operating-room environments.

