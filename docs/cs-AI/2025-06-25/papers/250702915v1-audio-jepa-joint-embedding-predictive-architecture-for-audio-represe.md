---
layout: default
title: "Audio-JEPA: Joint-Embedding Predictive Architecture for Audio Representation Learning"
---

# Audio-JEPA: Joint-Embedding Predictive Architecture for Audio Representation Learning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2507.02915" class="toolbar-btn" target="_blank">📄 arXiv: 2507.02915v1</a>
  <a href="https://arxiv.org/pdf/2507.02915.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2507.02915v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2507.02915v1', 'Audio-JEPA: Joint-Embedding Predictive Architecture for Audio Representation Learning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Ludovic Tuncay, Etienne Labbé, Emmanouil Benetos, Thomas Pellegrini

**分类**: cs.SD, cs.AI, cs.LG, eess.AS, eess.SP

**发布日期**: 2025-06-25

**期刊**: ICME 2025, Jun 2025, Nantes, France

---

## 💡 一句话要点

**提出Audio-JEPA以解决音频表示学习问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)**

**关键词**: `音频表示学习` `自监督学习` `联合嵌入` `视觉变换器` `声谱图`

## 📋 核心要点

1. 现有音频表示学习方法在数据利用效率和模型性能上存在不足，尤其是在缺乏标注数据的情况下。
2. Audio-JEPA通过预测掩蔽的声谱图块的潜在表示，采用简单的视觉变换器架构，避免了对原始音频的重建。
3. 实验结果表明，Audio-JEPA在多个音频任务上表现出与先进模型相当的性能，且训练数据需求显著降低。

## 📝 摘要（中文）

基于联合嵌入预测架构（JEPA）范式，本文提出了专门针对音频数据的Audio-JEPA。该方法利用简单的视觉变换器骨干网络，预测掩蔽的声谱图块的潜在表示，而不是重建原始音频。我们在未标记的AudioSet片段上进行预训练，并在X-ARES套件上进行评估，涵盖语音、音乐和环境声音任务。尽管实现是对原始模型的直接翻译，结果仍显示出与wav2vec 2.0和data2vec相当的性能，同时使用的训练数据不到其五分之一，且无需超参数调优。所有代码和预训练检查点将发布在GitHub上。

## 🔬 方法详解

**问题定义**：本文旨在解决音频表示学习中的数据利用效率低和模型性能不足的问题。现有方法如wav2vec 2.0和data2vec在训练过程中需要大量标注数据，且超参数调优复杂。

**核心思路**：Audio-JEPA的核心思路是通过联合嵌入预测架构，预测掩蔽的声谱图块的潜在表示，而非直接重建原始音频信号。这种方法能够有效利用未标记数据，提升模型的学习效率。

**技术框架**：Audio-JEPA的整体架构包括一个视觉变换器骨干网络，负责处理和预测声谱图的掩蔽块。预训练阶段使用随机掩蔽的mel声谱图进行训练，随后在多个音频任务上进行评估。

**关键创新**：最重要的技术创新在于将JEPA框架成功应用于音频数据，提出了一种新的音频表示学习方法，显著降低了对标注数据的依赖。

**关键设计**：在设计上，Audio-JEPA使用了简单的视觉变换器架构，并在训练过程中采用了随机掩蔽策略，损失函数设计为预测掩蔽块的潜在表示，确保模型能够有效学习音频特征。

## 📊 实验亮点

在实验中，Audio-JEPA在X-ARES套件上表现出与wav2vec 2.0和data2vec相当的性能，且训练数据需求不到其五分之一，且无需进行超参数调优，这表明其在音频表示学习中的有效性和高效性。

## 🎯 应用场景

Audio-JEPA的潜在应用场景包括语音识别、音乐推荐和环境声音分类等领域。其高效的音频表示学习能力能够为相关应用提供更强的支持，尤其是在标注数据稀缺的情况下，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Building on the Joint-Embedding Predictive Architecture (JEPA) paradigm, a recent self-supervised learning framework that predicts latent representations of masked regions in high-level feature spaces, we propose Audio-JEPA (Audio Joint-Embedding Predictive Architecture), tailored specifically for audio data. Audio-JEPA uses a simple Vision Transformer backbone to predict latent representations of masked spectrogram patches rather than reconstructing raw audio. We pre-train on unlabeled AudioSet clips (10s, 32kHz) with random patch masking on mel-spectrograms. We evaluate on the X-ARES suite covering speech, music, and environmental sound tasks. Although our implementation is a straightforward translation of the original model to audio, the results still show comparable performance to wav2vec 2.0 and data2vec while using less than one-fifth of their training data and with no hyper-parameter tuning. All code and pretrained checkpoints will be released on GitHub.

