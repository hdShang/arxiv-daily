---
layout: default
title: Benchmarking Egocentric Multimodal Goal Inference for Assistive Wearable Agents
---

# Benchmarking Egocentric Multimodal Goal Inference for Assistive Wearable Agents

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.22443" target="_blank" class="toolbar-btn">arXiv: 2510.22443v1</a>
    <a href="https://arxiv.org/pdf/2510.22443.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.22443v1" 
            onclick="toggleFavorite(this, '2510.22443v1', 'Benchmarking Egocentric Multimodal Goal Inference for Assistive Wearable Agents')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Vijay Veerabadran, Fanyi Xiao, Nitin Kamra, Pedro Matias, Joy Chen, Caley Drooff, Brett D Roads, Riley Williams, Ethan Henderson, Xuanyi Zhao, Kevin Carlberg, Joseph Tighe, Karl Ridgeway

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-25

**备注**: Accepted as a spotlight paper at the 39th Conference on Neural Information Processing Systems (NeurIPS 2025)

---

## 💡 一句话要点

**WAGIBench：用于辅助可穿戴代理的自中心多模态目标推断基准**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `自中心视觉` `多模态学习` `目标推断` `可穿戴设备` `视觉-语言模型`

## 📋 核心要点

1. 现有辅助可穿戴代理需要用户交互来明确目标，降低了用户体验，而自动目标推断可以解决此问题。
2. 论文提出WAGIBench基准，利用多模态数据（视觉、音频等）训练视觉-语言模型，实现用户意图的自动推断。
3. 实验表明，现有VLM模型在WAGIBench上表现与人类存在差距，但通过模态分析，可以提升模型性能。

## 📝 摘要（中文）

本文关注辅助可穿戴代理中的目标推断问题，旨在通过多模态上下文观察自动推断用户的目标，从而减少用户与代理交互所需的工作量。为此，作者构建了一个名为WAGIBench的基准，用于评估视觉-语言模型（VLMs）在此任务上的性能。该基准包含一个新颖的数据集，涵盖348名参与者的3477个记录，共计29小时的多模态数据，包括视觉、音频、数字和纵向上下文观察以及对应的ground-truth目标。实验结果表明，人类在此任务上的表现优于模型，多项选择准确率分别为93%和最佳VLM的84%。生成式基准测试表明，更大的模型表现更好，但距离实际应用仍有差距，仅在55%的情况下产生相关目标。模态消融实验表明，模型受益于相关模态的额外信息，而不相关模态对性能的影响很小。

## 🔬 方法详解

**问题定义**：论文旨在解决辅助可穿戴设备中，如何从用户的多模态上下文信息（视觉、听觉、数字交互等）中准确推断出用户当前目标的问题。现有方法通常需要用户主动输入或选择目标，效率较低，且不够自然。因此，自动化的目标推断是提升用户体验的关键。

**核心思路**：论文的核心思路是利用视觉-语言模型（VLM），将多模态的上下文信息编码为统一的语义表示，然后基于此表示推断用户的目标。通过构建大规模数据集WAGIBench，并在此数据集上训练和评估VLM，从而推动该领域的研究进展。

**技术框架**：整体框架包含数据采集、模型训练和评估三个主要阶段。数据采集阶段，通过可穿戴设备记录用户的多模态数据，并标注对应的目标。模型训练阶段，使用VLM模型学习多模态数据与目标之间的映射关系。评估阶段，使用WAGIBench数据集评估模型的性能，并与人类表现进行对比。

**关键创新**：论文的关键创新在于构建了WAGIBench数据集，该数据集是首个专门用于评估自中心多模态目标推断任务的大规模数据集。此外，论文还对多种VLM模型进行了基准测试，并分析了不同模态信息对模型性能的影响。

**关键设计**：WAGIBench数据集包含视觉、音频、数字交互和纵向上下文等多种模态的信息。在模型训练方面，论文采用了多种VLM模型，并针对目标推断任务进行了微调。在评估方面，论文采用了多项选择准确率和生成式评估指标，以全面评估模型的性能。

## 📊 实验亮点

实验结果表明，人类在WAGIBench数据集上的多项选择准确率为93%，而最佳VLM模型的准确率为84%，表明模型性能仍有提升空间。生成式基准测试显示，更大的模型表现更好，但仅在55%的情况下产生相关目标。模态消融实验表明，模型受益于相关模态的额外信息，而不相关模态对性能的影响很小。

## 🎯 应用场景

该研究成果可应用于智能眼镜、智能手表等可穿戴设备，实现更智能、更自然的辅助功能。例如，设备可以根据用户的行为和环境自动推断用户的需求，并提供相应的帮助，如导航、信息查询、设备控制等。这将极大地提升用户体验，并为残疾人士提供更便捷的生活辅助。

## 📄 摘要（原文）

> There has been a surge of interest in assistive wearable agents: agents embodied in wearable form factors (e.g., smart glasses) who take assistive actions toward a user's goal/query (e.g. "Where did I leave my keys?"). In this work, we consider the important complementary problem of inferring that goal from multi-modal contextual observations. Solving this "goal inference" problem holds the promise of eliminating the effort needed to interact with such an agent. This work focuses on creating WAGIBench, a strong benchmark to measure progress in solving this problem using vision-language models (VLMs). Given the limited prior work in this area, we collected a novel dataset comprising 29 hours of multimodal data from 348 participants across 3,477 recordings, featuring ground-truth goals alongside accompanying visual, audio, digital, and longitudinal contextual observations. We validate that human performance exceeds model performance, achieving 93% multiple-choice accuracy compared with 84% for the best-performing VLM. Generative benchmark results that evaluate several families of modern vision-language models show that larger models perform significantly better on the task, yet remain far from practical usefulness, as they produce relevant goals only 55% of the time. Through a modality ablation, we show that models benefit from extra information in relevant modalities with minimal performance degradation from irrelevant modalities.

