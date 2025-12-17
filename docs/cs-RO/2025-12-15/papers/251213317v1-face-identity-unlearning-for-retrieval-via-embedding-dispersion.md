---
layout: default
title: Face Identity Unlearning for Retrieval via Embedding Dispersion
---

# Face Identity Unlearning for Retrieval via Embedding Dispersion

**arXiv**: [2512.13317v1](https://arxiv.org/abs/2512.13317) | [PDF](https://arxiv.org/pdf/2512.13317.pdf)

**作者**: Mikhail Zakharov

---

## 💡 一句话要点

**提出基于嵌入分散的人脸身份遗忘方法，以保护检索系统中的隐私**

**关键词**: `人脸检索` `身份遗忘` `嵌入分散` `隐私保护` `机器学习遗忘`

## 📋 核心要点

1. 研究人脸检索中的身份遗忘问题，旨在使选定身份不可检索
2. 通过分散嵌入在超球面上，防止紧凑身份簇形成，同时保持其他身份的检索性能
3. 在VGGFace2和CelebA基准上验证方法，实现有效遗忘并保留检索效用

## 📄 摘要（原文）

> Face recognition systems rely on learning highly discriminative and compact identity clusters to enable accurate retrieval. However, as with other surveillance-oriented technologies, such systems raise serious privacy concerns due to their potential for unauthorized identity tracking. While several works have explored machine unlearning as a means of privacy protection, their applicability to face retrieval - especially for modern embedding-based recognition models - remains largely unexplored. In this work, we study the problem of face identity unlearning for retrieval systems and present its inherent challenges. The goal is to make selected identities unretrievable by dispersing their embeddings on the hypersphere and preventing the formation of compact identity clusters that enable re-identification in the gallery. The primary challenge is to achieve this forgetting effect while preserving the discriminative structure of the embedding space and the retrieval performance of the model for the remaining identities. To address this, we evaluate several existing approximate class unlearning methods (e.g., Random Labeling, Gradient Ascent, Boundary Unlearning, and other recent approaches) in the context of face retrieval and propose a simple yet effective dispersion-based unlearning approach. Extensive experiments on standard benchmarks (VGGFace2, CelebA) demonstrate that our method achieves superior forgetting behavior while preserving retrieval utility.

