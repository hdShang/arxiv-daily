---
layout: default
title: FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling
---

# FacEDiT: Unified Talking Face Editing and Generation via Facial Motion Infilling

**arXiv**: [2512.14056v1](https://arxiv.org/abs/2512.14056) | [PDF](https://arxiv.org/pdf/2512.14056.pdf)

**作者**: Kim Sung-Bin, Joohyun Chang, David Harwath, Tae-Hyun Oh

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

**备注**: Project page: https://facedit.github.io/

---

## 💡 一句话要点

**提出FacEDiT，通过语音条件面部运动填充统一处理说话人脸编辑与生成问题。**

**关键词**: `说话人脸编辑` `面部运动填充` `扩散变换器` `语音条件合成` `自监督学习` `多模态融合` `视频生成` `唇部同步`

## 📋 核心要点

1. 核心问题：现有方法将说话人脸编辑和生成视为独立任务，缺乏统一框架，导致编辑时边界不连续和身份保持差。
2. 方法要点：提出语音条件面部运动填充作为统一框架，使用扩散变换器学习掩码面部运动合成，结合偏置注意力和平滑约束。
3. 实验或效果：FacEDiT在编辑和生成任务中均表现优异，实现高精度唇部同步、身份保持和视觉连续性，并引入新基准验证。

## 📝 摘要（中文）

说话人脸编辑和生成通常被视为独立问题。本研究提出将两者视为统一框架——语音条件面部运动填充的子任务。我们探索面部运动填充作为一种自监督预训练任务，同时作为动态说话人脸合成的统一表述。为实现这一想法，我们提出FacEDiT，一种基于流匹配训练的语音条件扩散变换器。受掩码自编码器启发，FacEDiT学习在周围运动和语音条件下合成掩码面部运动。这一框架支持局部生成和编辑，如替换、插入和删除，同时确保与未编辑区域的无缝过渡。此外，偏置注意力和时间平滑性约束增强了边界连续性和唇部同步。针对缺乏标准编辑基准的问题，我们引入FacEDiTBench，首个说话人脸编辑数据集，包含多样编辑类型和长度，以及新评估指标。大量实验验证说话人脸编辑和生成作为语音条件运动填充的子任务；FacEDiT产生准确、语音对齐的面部编辑，具有强身份保持和流畅视觉连续性，同时有效泛化到说话人脸生成。

## 🔬 方法详解

FacEDiT的整体框架基于语音条件扩散变换器，采用流匹配训练。关键技术创新点包括：将面部运动填充作为自监督预训练任务，统一说话人脸编辑与生成；受掩码自编码器启发，模型学习在周围运动和语音条件下合成掩码面部运动；引入偏置注意力和时间平滑性约束以增强边界连续性和唇部同步。与现有方法的主要区别在于，传统方法通常分别处理编辑和生成，而FacEDiT通过统一框架实现两者，支持局部编辑如替换、插入和删除，同时确保无缝过渡。

## 📊 实验亮点

实验显示FacEDiT在说话人脸编辑和生成任务中均优于基线方法，实现准确语音对齐、强身份保持和流畅视觉连续性；新基准FacEDiTBench验证了模型在多样编辑类型下的泛化能力，性能提升显著。

## 🎯 应用场景

该研究在虚拟现实、视频会议、电影特效和数字人交互等领域有广泛应用潜力，可实现高保真说话人脸编辑和生成，提升用户体验和内容创作效率。

## 📄 摘要（原文）

> Talking face editing and face generation have often been studied as distinct problems. In this work, we propose viewing both not as separate tasks but as subtasks of a unifying formulation, speech-conditional facial motion infilling. We explore facial motion infilling as a self-supervised pretext task that also serves as a unifying formulation of dynamic talking face synthesis. To instantiate this idea, we propose FacEDiT, a speech-conditional Diffusion Transformer trained with flow matching. Inspired by masked autoencoders, FacEDiT learns to synthesize masked facial motions conditioned on surrounding motions and speech. This formulation enables both localized generation and edits, such as substitution, insertion, and deletion, while ensuring seamless transitions with unedited regions. In addition, biased attention and temporal smoothness constraints enhance boundary continuity and lip synchronization. To address the lack of a standard editing benchmark, we introduce FacEDiTBench, the first dataset for talking face editing, featuring diverse edit types and lengths, along with new evaluation metrics. Extensive experiments validate that talking face editing and generation emerge as subtasks of speech-conditional motion infilling; FacEDiT produces accurate, speech-aligned facial edits with strong identity preservation and smooth visual continuity while generalizing effectively to talking face generation.

