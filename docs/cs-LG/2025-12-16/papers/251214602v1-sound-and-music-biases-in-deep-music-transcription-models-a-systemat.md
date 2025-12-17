---
layout: default
title: Sound and Music Biases in Deep Music Transcription Models: A Systematic Analysis
---

# Sound and Music Biases in Deep Music Transcription Models: A Systematic Analysis

**arXiv**: [2512.14602v1](https://arxiv.org/abs/2512.14602) | [PDF](https://arxiv.org/pdf/2512.14602.pdf)

**作者**: Lukáš Samuel Marták, Patricia Hu, Gerhard Widmer

**分类**: cs.SD, cs.LG

**发布日期**: 2025-12-16

**备注**: pre-print of the upcoming EURASIP JASM journal article

**DOI**: [10.1186/s13636-025-00428-z](https://doi.org/10.1186/s13636-025-00428-z)

---

## 💡 一句话要点

**系统分析深度音乐转录模型中的声音与音乐偏见，揭示其在分布偏移下的性能退化问题。**

🎯 **匹配领域**: **强化学习**

**关键词**: `自动音乐转录` `分布偏移` `语料库偏见` `音乐感知评估` `深度学习` `泛化能力` `性能退化` `MDS语料库`

## 📋 核心要点

1. 核心问题：深度AMT模型因训练数据集中于古典钢琴音乐，泛化能力受限，对流派、动态等音乐变化敏感。
2. 方法要点：引入MDS语料库模拟分布偏移，结合传统和音乐感知指标，系统评估模型在声音与音乐维度上的性能。
3. 实验或效果：发现音符级F1性能因声音下降20个百分点，因流派下降14个百分点，动态估计更易受音乐变化影响。

## 📝 摘要（中文）

自动音乐转录（AMT）——将音乐音频转换为音符表示的任务——在深度学习系统的推动下取得了快速进展。由于丰富标注音乐数据集的可用性有限，AMT的大部分进展集中在古典钢琴音乐，甚至少数特定数据集上。这些系统是否能有效泛化到其他音乐背景仍是一个开放问题。本研究补充了最近关于声音分布偏移（如录音条件）的研究，调查了音乐维度——特别是流派、动态和复音水平的变化。为此，我们引入了MDS语料库，包含三个不同子集——（1）流派，（2）随机，和（3）MAEtest——以模拟分布偏移的不同轴。我们使用传统信息检索和音乐感知性能指标评估了多个最先进AMT系统在MDS语料库上的表现。广泛的评估隔离并暴露了在特定分布偏移下不同程度的性能退化。特别是，我们测量到由于声音导致的音符级F1性能下降20个百分点，由于流派导致的下降14个百分点。总体而言，我们发现动态估计比起始预测更容易受到音乐变化的影响。音乐感知评估指标，特别是那些捕捉和声结构的指标，有助于识别潜在贡献因素。此外，随机生成的非音乐序列实验揭示了在极端音乐分布偏移下系统性能的明显限制。总之，这些发现为深度AMT系统中语料库偏见问题的持续影响提供了新证据。

## 🔬 方法详解

论文的核心方法是引入MDS语料库作为评估框架，包含Genre、Random和MAEtest三个子集，以模拟音乐流派、随机序列和特定测试条件下的分布偏移。整体框架涉及使用多个最先进的深度AMT模型，在MDS语料库上进行系统评估，结合传统信息检索指标（如F1分数）和音乐感知指标（如捕捉和声结构的指标）。关键技术创新点在于将音乐维度（如流派、动态、复音水平）作为分布偏移轴进行量化分析，与现有方法主要关注声音条件偏移形成区别。主要区别在于本研究不仅评估模型在标准数据集上的性能，还通过设计多样化测试集来揭示模型在真实世界音乐变化中的泛化瓶颈。

## 📊 实验亮点

最重要的实验结果显示，音符级F1性能在声音分布偏移下下降20个百分点，在流派偏移下下降14个百分点；动态估计比起始预测更脆弱；随机非音乐序列实验暴露了模型在极端偏移下的性能限制。

## 🎯 应用场景

该研究可应用于改进自动音乐转录系统的鲁棒性，支持音乐教育、音乐信息检索和音频编辑工具的开发，通过识别和缓解偏见，提升模型在多样化音乐场景（如流行音乐、现场录音）中的实用价值。

## 📄 摘要（原文）

> Automatic Music Transcription (AMT) -- the task of converting music audio into note representations -- has seen rapid progress, driven largely by deep learning systems. Due to the limited availability of richly annotated music datasets, much of the progress in AMT has been concentrated on classical piano music, and even a few very specific datasets. Whether these systems can generalize effectively to other musical contexts remains an open question. Complementing recent studies on distribution shifts in sound (e.g., recording conditions), in this work we investigate the musical dimension -- specifically, variations in genre, dynamics, and polyphony levels. To this end, we introduce the MDS corpus, comprising three distinct subsets -- (1) Genre, (2) Random, and (3) MAEtest -- to emulate different axes of distribution shift. We evaluate the performance of several state-of-the-art AMT systems on the MDS corpus using both traditional information-retrieval and musically-informed performance metrics. Our extensive evaluation isolates and exposes varying degrees of performance degradation under specific distribution shifts. In particular, we measure a note-level F1 performance drop of 20 percentage points due to sound, and 14 due to genre. Generally, we find that dynamics estimation proves more vulnerable to musical variation than onset prediction. Musically informed evaluation metrics, particularly those capturing harmonic structure, help identify potential contributing factors. Furthermore, experiments with randomly generated, non-musical sequences reveal clear limitations in system performance under extreme musical distribution shifts. Altogether, these findings offer new evidence of the persistent impact of the Corpus Bias problem in deep AMT systems.

