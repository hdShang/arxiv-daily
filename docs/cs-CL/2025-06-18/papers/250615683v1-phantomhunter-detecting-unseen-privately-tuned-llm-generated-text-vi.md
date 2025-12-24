---
layout: default
title: "PhantomHunter: Detecting Unseen Privately-Tuned LLM-Generated Text via Family-Aware Learning"
---

# PhantomHunter: Detecting Unseen Privately-Tuned LLM-Generated Text via Family-Aware Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15683" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15683v1</a>
  <a href="https://arxiv.org/pdf/2506.15683.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15683v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15683v1', 'PhantomHunter: Detecting Unseen Privately-Tuned LLM-Generated Text via Family-Aware Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yuhui Shi, Yehan Yang, Qiang Sheng, Hao Mi, Beizhe Hu, Chaoxi Xu, Juan Cao

**分类**: cs.CL, cs.CY

**发布日期**: 2025-06-18

**备注**: 17 pages, 3 figures, 6 tables

---

## 💡 一句话要点

**提出PhantomHunter以解决未见私有调优LLM生成文本检测问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `大型语言模型` `文本检测` `家族感知学习` `私有调优` `虚假信息识别` `机器学习` `自然语言处理`

## 📋 核心要点

1. 现有的LLM生成文本检测方法在面对私有调优的LLM生成文本时性能显著下降，未能有效应对这一新挑战。
2. PhantomHunter采用家族感知学习框架，专注于捕捉基础模型及其衍生模型之间的共享特征，从而提高检测能力。
3. 实验结果显示，PhantomHunter在多个数据集上表现优越，F1分数超过96%，明显优于现有的7个基线和3个工业服务。

## 📝 摘要（中文）

随着大型语言模型（LLMs）的普及，虚假信息和学术不端等社会问题愈发严重，使得LLM生成文本的检测变得前所未有的重要。现有方法虽然取得了显著进展，但针对私有调优LLM生成文本的新挑战尚未得到充分探索。用户可以通过用私有语料微调开源模型轻松获得私有LLM，这导致现有检测器在实际应用中的性能显著下降。为了解决这一问题，我们提出了PhantomHunter，这是一种专门用于检测来自未见私有调优LLM的文本的检测器。其家族感知学习框架捕捉基础模型及其衍生模型之间共享的家族级特征，而不是记忆个体特征。实验结果表明，PhantomHunter在LLaMA、Gemma和Mistral家族的数据上优于7个基线和3个工业服务，F1分数超过96%。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有LLM生成文本检测方法在面对未见私有调优LLM生成文本时的性能下降问题。现有方法主要依赖于个体特征的记忆，无法有效应对新出现的文本类型。

**核心思路**：PhantomHunter的核心思路是采用家族感知学习框架，关注基础模型及其衍生模型之间的共享特征，而非单一模型的特征，从而提高检测的泛化能力。

**技术框架**：整体架构包括数据预处理、特征提取、模型训练和评估四个主要模块。首先，通过数据预处理模块清洗和准备数据，然后在特征提取模块中提取家族级特征，接着在模型训练阶段进行家族感知学习，最后通过评估模块验证模型性能。

**关键创新**：PhantomHunter的关键创新在于其家族感知学习框架，这一设计使得模型能够捕捉到不同模型之间的共性特征，显著提高了对未见文本的检测能力，与现有方法的个体特征记忆形成鲜明对比。

**关键设计**：在模型设计中，采用了特定的损失函数以优化家族特征的学习，同时在网络结构上引入了多层次特征提取机制，以增强模型的表达能力和泛化能力。具体参数设置和网络结构细节在论文中有详细描述。

## 📊 实验亮点

在实验中，PhantomHunter在LLaMA、Gemma和Mistral家族的数据集上表现出色，F1分数超过96%。与7个基线和3个工业服务相比，PhantomHunter的性能显著提升，展示了其在未见私有调优LLM生成文本检测中的优越性。

## 🎯 应用场景

PhantomHunter的研究成果在多个领域具有潜在应用价值，特别是在社交媒体、新闻出版和学术研究等领域，可以有效识别和防止虚假信息的传播。此外，该技术还可以为内容审核和合规性检查提供支持，确保信息的真实性和可靠性。未来，随着LLM技术的进一步发展，PhantomHunter有望成为文本检测领域的标准工具。

## 📄 摘要（原文）

> With the popularity of large language models (LLMs), undesirable societal problems like misinformation production and academic misconduct have been more severe, making LLM-generated text detection now of unprecedented importance. Although existing methods have made remarkable progress, a new challenge posed by text from privately tuned LLMs remains underexplored. Users could easily possess private LLMs by fine-tuning an open-source one with private corpora, resulting in a significant performance drop of existing detectors in practice. To address this issue, we propose PhantomHunter, an LLM-generated text detector specialized for detecting text from unseen, privately-tuned LLMs. Its family-aware learning framework captures family-level traits shared across the base models and their derivatives, instead of memorizing individual characteristics. Experiments on data from LLaMA, Gemma, and Mistral families show its superiority over 7 baselines and 3 industrial services, with F1 scores of over 96%.

