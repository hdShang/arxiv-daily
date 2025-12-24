---
layout: default
title: EEG-to-Text Translation: A Model for Deciphering Human Brain Activity
---

# EEG-to-Text Translation: A Model for Deciphering Human Brain Activity

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.13936" class="toolbar-btn" target="_blank">📄 arXiv: 2505.13936v2</a>
  <a href="https://arxiv.org/pdf/2505.13936.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.13936v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.13936v2', 'EEG-to-Text Translation: A Model for Deciphering Human Brain Activity')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Saydul Akbar Murad, Ashim Dahal, Nick Rahimi

**分类**: cs.CL, cs.AI

**发布日期**: 2025-05-20 (更新: 2025-12-08)

**🔗 代码/项目**: [GITHUB](https://github.com/Mmurrad/EEG-To-text)

---

## 💡 一句话要点

**提出R1 Translator以提升脑电图到文本翻译性能**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `脑电图解码` `文本生成` `双向LSTM` `变换器模型` `机器学习` `人机交互` `脑机接口`

## 📋 核心要点

1. 现有EEG到文本解码模型在性能上存在显著限制，难以满足实际应用需求。
2. 本文提出的R1 Translator模型结合了双向LSTM编码器和预训练的变换器解码器，以提高解码质量。
3. R1 Translator在ROUGE、CER和WER等指标上均优于T5和Brain Translator，显示出显著的性能提升。

## 📝 摘要（中文）

随着大型语言模型如Gemini和GPT的快速发展，连接人脑与语言处理的研究变得愈发重要。为了解决脑电图（EEG）信号解码为文本的挑战，研究者们提出了多种模型。然而，这些模型在性能上仍存在显著限制。本文提出了一种新模型R1 Translator，旨在改善EEG到文本解码的性能。R1 Translator结合了双向LSTM编码器和预训练的基于变换器的解码器，利用EEG特征生成高质量文本输出。实验结果显示，R1在ROUGE指标上表现优异，超越了T5和Brain Translator，具体ROUGE-1得分为38.00%，比T5高出9%。

## 🔬 方法详解

**问题定义**：本文旨在解决脑电图（EEG）信号解码为文本的性能不足问题。现有模型在解码精度和文本质量上存在显著短板，限制了其实际应用。

**核心思路**：R1 Translator模型通过结合双向LSTM和预训练的变换器，旨在更好地捕捉EEG信号的时序特征，从而提升文本生成的质量和准确性。

**技术框架**：该模型的整体架构包括两个主要模块：首先，使用双向LSTM编码器处理EEG嵌入，以捕捉信号的时序依赖；其次，将LSTM的输出传递给变换器解码器，进行文本生成。

**关键创新**：R1 Translator的主要创新在于将双向LSTM与变换器解码器相结合，利用LSTM捕捉时序信息，显著提升了文本生成的质量，区别于以往单一模型的设计。

**关键设计**：在模型设计中，采用了特定的损失函数以优化文本生成效果，同时在网络结构上，LSTM和变换器的结合使得模型能够更有效地处理EEG信号。

## 📊 实验亮点

R1 Translator在多个性能指标上均表现优异，ROUGE-1得分达到38.00%，比T5高出9%；在ROUGE-L上，F1得分为32.51%，超越T5和Brain Translator；CER和WER分别为0.5795和0.7280，显示出显著的性能提升。

## 🎯 应用场景

该研究的潜在应用领域包括脑机接口、医疗诊断和人机交互等。通过提高EEG信号解码的准确性，R1 Translator能够为脑电图分析提供更为可靠的工具，推动相关领域的发展，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> With the rapid advancement of large language models like Gemini, GPT, and others, bridging the gap between the human brain and language processing has become an important area of focus. To address this challenge, researchers have developed various models to decode EEG signals into text. However, these models still face significant performance limitations. To overcome these shortcomings, we propose a new model, R1 Translator, which aims to improve the performance of EEG-to-text decoding. The R1 Translator model combines a bidirectional LSTM encoder with a pretrained transformer-based decoder, utilizing EEG features to produce high-quality text outputs. The model processes EEG embeddings through the LSTM to capture sequential dependencies, which are then fed into the transformer decoder for effective text generation. The R1 Translator excels in ROUGE metrics, outperforming both T5 (previous research) and Brain Translator. Specifically, R1 achieves a ROUGE-1 score of 38.00% (P), which is up to 9% higher than T5 (34.89%) and 3% better than Brain (35.69%). It also leads in ROUGE-L, with a F1 score of 32.51%, outperforming T5 by 3% (29.67%) and Brain by 2% (30.38%). In terms of CER, R1 achieves a CER of 0.5795, which is 2% lower than T5 (0.5917) and 4% lower than Brain (0.6001). Additionally, R1 performs better in WER with a score of 0.7280, outperforming T5 by 4.3% (0.7610) and Brain by 3.6% (0.7553). Code is available at https://github.com/Mmurrad/EEG-To-text.

