---
layout: default
title: Semantic-Consistent Bidirectional Contrastive Hashing for Noisy Multi-Label Cross-Modal Retrieval
---

# Semantic-Consistent Bidirectional Contrastive Hashing for Noisy Multi-Label Cross-Modal Retrieval

**arXiv**: [2511.07780v1](https://arxiv.org/abs/2511.07780) | [PDF](https://arxiv.org/pdf/2511.07780.pdf)

**作者**: Likang Peng, Chao Su, Wenyuan Wu, Yuan Sun, Dezhong Peng, Xi Peng, Xu Wang

---

## 💡 一句话要点

**提出语义一致双向对比哈希以解决噪声多标签跨模态检索问题**

**关键词**: `跨模态哈希` `多标签检索` `噪声标签处理` `对比学习` `语义一致性`

## 📋 核心要点

1. 核心问题：多标签数据中标签噪声和语义重叠未被充分处理，影响检索性能。
2. 方法要点：结合跨模态语义一致分类和双向软对比哈希，动态生成样本对。
3. 实验或效果：在四个基准数据集上验证，噪声条件下优于现有方法。

## 📄 摘要（原文）

> Cross-modal hashing (CMH) facilitates efficient retrieval across different modalities (e.g., image and text) by encoding data into compact binary representations. While recent methods have achieved remarkable performance, they often rely heavily on fully annotated datasets, which are costly and labor-intensive to obtain. In real-world scenarios, particularly in multi-label datasets, label noise is prevalent and severely degrades retrieval performance. Moreover, existing CMH approaches typically overlook the partial semantic overlaps inherent in multi-label data, limiting their robustness and generalization. To tackle these challenges, we propose a novel framework named Semantic-Consistent Bidirectional Contrastive Hashing (SCBCH). The framework comprises two complementary modules: (1) Cross-modal Semantic-Consistent Classification (CSCC), which leverages cross-modal semantic consistency to estimate sample reliability and reduce the impact of noisy labels; (2) Bidirectional Soft Contrastive Hashing (BSCH), which dynamically generates soft contrastive sample pairs based on multi-label semantic overlap, enabling adaptive contrastive learning between semantically similar and dissimilar samples across modalities. Extensive experiments on four widely-used cross-modal retrieval benchmarks validate the effectiveness and robustness of our method, consistently outperforming state-of-the-art approaches under noisy multi-label conditions.

