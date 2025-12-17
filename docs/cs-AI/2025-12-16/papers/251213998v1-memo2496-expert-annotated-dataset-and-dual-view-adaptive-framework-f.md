---
layout: default
title: Memo2496: Expert-Annotated Dataset and Dual-View Adaptive Framework for Music Emotion Recognition
---

# Memo2496: Expert-Annotated Dataset and Dual-View Adaptive Framework for Music Emotion Recognition

**arXiv**: [2512.13998v1](https://arxiv.org/abs/2512.13998) | [PDF](https://arxiv.org/pdf/2512.13998.pdf)

**作者**: Qilin Li, C. L. Philip Chen, TongZhang

**分类**: cs.SD, cs.AI, cs.MM

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出Memo2496数据集和DAMER框架以解决音乐情感识别中数据质量低和跨曲目特征漂移问题**

**关键词**: `音乐情感识别` `多模态融合` `伪标签生成` `特征漂移缓解` `对比学习` `注意力机制` `数据集构建` `自适应学习`

## 📋 核心要点

1. 音乐情感识别面临高质量标注数据稀缺和跨曲目特征漂移的挑战，现有方法难以稳定处理不同音乐风格的情感表达。
2. 提出DAMER框架，集成双流注意力融合、渐进置信度标注和风格锚定记忆学习模块，协同提升特征交互和泛化能力。
3. 在多个数据集上实现显著性能提升，唤醒维度准确率最高提升3.43%，并通过消融实验验证各模块有效性。

## 📝 摘要（中文）

音乐情感识别研究面临高质量标注数据集有限和跨曲目特征漂移的挑战。本文提出两项主要贡献：Memo2496是一个大规模数据集，包含2496首器乐曲目，由30位认证音乐专家标注连续效价-唤醒度标签，通过极端情感示例校准和效价-唤醒空间欧氏距离一致性阈值0.25确保标注质量；同时提出双视图自适应音乐情感识别器，集成三个协同模块：双流注意力融合通过交叉注意力机制促进梅尔频谱图和耳蜗图之间的令牌级双向交互，渐进置信度标注采用课程式温度调度和Jensen-Shannon散度一致性量化生成可靠伪标签，风格锚定记忆学习维护对比记忆队列以缓解跨曲目特征漂移。在Memo2496、1000songs和PMEmo数据集上的广泛实验表明DAMER达到最先进性能，唤醒维度准确率分别提升3.43%、2.25%和0.17%，消融研究和可视化分析验证了各模块贡献。数据集和源代码已公开。

## 🔬 方法详解

DAMER框架采用双视图自适应架构，核心创新在于三个模块：双流注意力融合实现梅尔频谱图和耳蜗图的令牌级双向交互，增强多模态特征融合；渐进置信度标注通过课程式温度调度和Jensen-Shannon散度量化生成高质量伪标签，提升训练稳定性；风格锚定记忆学习利用对比记忆队列缓解跨曲目特征漂移，提高模型泛化性。与现有方法相比，DAMER首次系统整合多模态交互、伪标签优化和特征漂移缓解，形成端到端的自适应学习系统。

## 📊 实验亮点

DAMER在Memo2496、1000songs和PMEmo数据集上唤醒维度准确率分别提升3.43%、2.25%和0.17%，达到最先进性能；消融研究证实各模块均贡献显著，可视化分析进一步验证了特征漂移缓解效果。

## 🎯 应用场景

该研究可应用于智能音乐推荐系统、情感化音乐治疗、影视配乐自动生成等领域，通过精准识别音乐情感，提升用户体验和个性化服务，具有广泛的娱乐、医疗和创作价值。

## 📄 摘要（原文）

> Music Emotion Recogniser (MER) research faces challenges due to limited high-quality annotated datasets and difficulties in addressing cross-track feature drift. This work presents two primary contributions to address these issues. Memo2496, a large-scale dataset, offers 2496 instrumental music tracks with continuous valence arousal labels, annotated by 30 certified music specialists. Annotation quality is ensured through calibration with extreme emotion exemplars and a consistency threshold of 0.25, measured by Euclidean distance in the valence arousal space. Furthermore, the Dual-view Adaptive Music Emotion Recogniser (DAMER) is introduced. DAMER integrates three synergistic modules: Dual Stream Attention Fusion (DSAF) facilitates token-level bidirectional interaction between Mel spectrograms and cochleagrams via cross attention mechanisms; Progressive Confidence Labelling (PCL) generates reliable pseudo labels employing curriculum-based temperature scheduling and consistency quantification using Jensen Shannon divergence; and Style Anchored Memory Learning (SAML) maintains a contrastive memory queue to mitigate cross-track feature drift. Extensive experiments on the Memo2496, 1000songs, and PMEmo datasets demonstrate DAMER's state-of-the-art performance, improving arousal dimension accuracy by 3.43%, 2.25%, and 0.17%, respectively. Ablation studies and visualisation analyses validate each module's contribution. Both the dataset and source code are publicly available.

