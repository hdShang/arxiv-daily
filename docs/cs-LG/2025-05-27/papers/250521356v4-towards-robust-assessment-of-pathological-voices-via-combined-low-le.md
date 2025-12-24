---
layout: default
title: Towards Robust Assessment of Pathological Voices via Combined Low-Level Descriptors and Foundation Model Representations
---

# Towards Robust Assessment of Pathological Voices via Combined Low-Level Descriptors and Foundation Model Representations

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.21356" class="toolbar-btn" target="_blank">📄 arXiv: 2505.21356v4</a>
  <a href="https://arxiv.org/pdf/2505.21356.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.21356v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.21356v4', 'Towards Robust Assessment of Pathological Voices via Combined Low-Level Descriptors and Foundation Model Representations')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Whenty Ariyanti, Kuan-Yu Chen, Sabato Marco Siniscalchi, Hsin-Min Wang, Yu Tsao

**分类**: cs.SD, cs.LG, eess.AS

**发布日期**: 2025-05-27 (更新: 2025-12-11)

---

## 💡 一句话要点

**提出VOQANet及其增强版以解决病理声音评估问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `声音质量评估` `深度学习` `语音基础模型` `低层声学特征` `鲁棒性` `医疗诊断` `自监督学习`

## 📋 核心要点

1. 现有的声音质量评估方法依赖于专家评估，存在评估者间的变异性，缺乏客观性。
2. 本研究提出了VOQANet深度学习框架，结合注意力机制和SFM嵌入，提取高层特征以提高评估准确性。
3. 实验结果显示，VOQANet在CAPE-V和GRBAS维度上优于基线模型，VOQANet+在噪声条件下表现出更强的鲁棒性。

## 📝 摘要（中文）

感知声音质量评估在诊断和监测声音障碍中至关重要。传统方法如CAPE-V和GRBAS依赖专家评估，存在评估者间的变异性，因此需要客观解决方案。本研究提出了声音质量评估网络（VOQANet），该深度学习框架利用注意力机制和语音基础模型（SFM）嵌入提取高层特征。为进一步提升性能，我们提出了VOQANet+，将自监督SFM嵌入与低层声学描述符（如抖动、闪烁和噪声比）结合。与以往仅关注元音发声的模型不同，我们的模型在元音级和句子级语音上进行评估，以检验其泛化能力。实验结果表明，基于句子的输入在患者级别上具有更高的准确性，VOQANet在CAPE-V和GRBAS维度上均优于基线模型，VOQANet+更是实现了显著的性能提升。

## 🔬 方法详解

**问题定义**：本论文旨在解决病理声音评估中存在的主观性和评估者间变异性的问题。传统方法依赖专家评估，缺乏客观性和一致性。

**核心思路**：提出VOQANet深度学习框架，结合注意力机制和语音基础模型（SFM）嵌入，提取高层特征，同时引入低层声学描述符以增强模型性能。

**技术框架**：VOQANet的整体架构包括特征提取模块、注意力机制模块和评估模块。特征提取模块负责从输入语音中提取高层和低层特征，注意力机制模块增强重要特征的权重，评估模块则进行最终的声音质量评分。

**关键创新**：最重要的创新在于将SFM嵌入与低层声学特征结合，形成VOQANet+，这使得模型在多种发声方式下均能保持高准确性，尤其是在句子级评估中表现优异。

**关键设计**：模型采用自监督学习策略，损失函数设计为结合RMSE和Pearson相关系数，以优化模型在不同评估维度上的表现。网络结构上，采用多层卷积神经网络（CNN）和循环神经网络（RNN）相结合的方式，以捕捉时间序列特征。

## 📊 实验亮点

实验结果表明，VOQANet在CAPE-V和GRBAS维度上均优于基线模型，特别是在患者级别上，句子级输入的准确性显著提高。VOQANet+在噪声条件下表现出更强的鲁棒性，进一步提升了评估的可靠性和实用性。

## 🎯 应用场景

该研究的潜在应用领域包括医疗诊断、远程健康监测和语音治疗等。通过提供更客观和一致的声音质量评估工具，能够帮助医生更好地诊断和监测声音障碍，提升患者的治疗效果。未来，该技术有望在智能语音助手和语音识别系统中得到应用，提升其对病理声音的识别能力。

## 📄 摘要（原文）

> Perceptual voice quality assessment plays a vital role in diagnosing and monitoring voice disorders. Traditional methods, such as the Consensus Auditory-Perceptual Evaluation of Voice (CAPE-V) and the Grade, Roughness, Breathiness, Asthenia, and Strain (GRBAS) scales, rely on expert raters and are prone to inter-rater variability, emphasizing the need for objective solutions. This study introduces the Voice Quality Assessment Network (VOQANet), a deep learning framework that employs an attention mechanism and Speech Foundation Model (SFM) embeddings to extract high-level features. To further enhance performance, we propose VOQANet+, which integrates self-supervised SFM embeddings with low-level acoustic descriptors-namely jitter, shimmer, and harmonics-to-noise ratio (HNR). Unlike previous approaches that focus solely on vowel-based phonation (PVQD-A), our models are evaluated on both vowel-level and sentence-level speech (PVQD-S) to assess generalizability. Experimental results demonstrate that sentence-based inputs yield higher accuracy, particularly at the patient level. Overall, VOQANet consistently outperforms baseline models in terms of root mean squared error (RMSE) and Pearson correlation coefficient across CAPE-V and GRBAS dimensions, with VOQANet+ achieving even greater performance gains. Additionally, VOQANet+ maintains consistent performance under noisy conditions, suggesting enhanced robustness for real-world and telehealth applications. This work highlights the value of combining SFM embeddings with low-level features for accurate and robust pathological voice assessment.

