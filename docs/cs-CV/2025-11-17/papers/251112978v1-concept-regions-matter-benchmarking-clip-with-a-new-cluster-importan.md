---
layout: default
title: Concept Regions Matter: Benchmarking CLIP with a New Cluster-Importance Approach
---

# Concept Regions Matter: Benchmarking CLIP with a New Cluster-Importance Approach

**arXiv**: [2511.12978v1](https://arxiv.org/abs/2511.12978) | [PDF](https://arxiv.org/pdf/2511.12978.pdf)

**作者**: Aishwarya Agarwal, Srikrishna Karanam, Vineet Gandhi

---

## 💡 一句话要点

**提出CCI方法以评估CLIP模型对虚假相关性的鲁棒性**

**关键词**: `视觉语言模型` `解释性方法` `虚假相关性` `基准测试` `聚类分析` `零样本识别`

## 📋 核心要点

1. CLIP等视觉语言模型易受背景虚假相关性影响，导致预测偏差
2. CCI利用补丁嵌入聚类和掩码，评估预测变化，提升解释性
3. 结合COVAR基准，系统评估18个CLIP变体，推动模型鲁棒性

## 📄 摘要（原文）

> Contrastive vision-language models (VLMs) such as CLIP achieve strong zero-shot recognition yet remain vulnerable to spurious correlations, particularly background over-reliance. We introduce Cluster-based Concept Importance (CCI), a novel interpretability method that uses CLIP's own patch embeddings to group spatial patches into semantically coherent clusters, mask them, and evaluate relative changes in model predictions. CCI sets a new state of the art on faithfulness benchmarks, surpassing prior methods by large margins; for example, it yields more than a twofold improvement on the deletion-AUC metric for MS COCO retrieval. We further propose that CCI, when combined with GroundedSAM, automatically categorizes predictions as foreground- or background-driven, providing a crucial diagnostic ability. Existing benchmarks such as CounterAnimals, however, rely solely on accuracy and implicitly attribute all performance degradation to background correlations. Our analysis shows this assumption to be incomplete, since many errors arise from viewpoint variation, scale shifts, and fine-grained object confusions. To disentangle these effects, we introduce COVAR, a benchmark that systematically varies object foregrounds and backgrounds. Leveraging CCI with COVAR, we present a comprehensive evaluation of eighteen CLIP variants, offering methodological advances and empirical evidence that chart a path toward more robust VLMs.

