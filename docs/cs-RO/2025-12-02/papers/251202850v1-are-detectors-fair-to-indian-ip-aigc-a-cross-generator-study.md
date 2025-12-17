---
layout: default
title: Are Detectors Fair to Indian IP-AIGC? A Cross-Generator Study
---

# Are Detectors Fair to Indian IP-AIGC? A Cross-Generator Study

**arXiv**: [2512.02850v1](https://arxiv.org/abs/2512.02850) | [PDF](https://arxiv.org/pdf/2512.02850.pdf)

**作者**: Vishal Dubey, Pallavi Tyagi

---

## 💡 一句话要点

**评估印度IP-AIGC检测器的公平性与泛化性，揭示跨生成器性能下降问题。**

**关键词**: `身份保持AIGC检测` `公平性评估` `跨生成器泛化` `印度人脸数据集` `微调过拟合` `AIGC检测基准`

## 📋 核心要点

1. 研究现代图像编辑器生成的印度身份保持AIGC检测的公平性，关注代表性不足人群。
2. 构建印度焦点训练集和IP-AIGC测试集，评估AIDE和Effort检测器在预训练与微调下的性能。
3. 发现微调虽提升域内性能，但在跨生成器IP-AIGC上泛化性下降，表明过拟合训练生成器线索。

## 📄 摘要（原文）

> Modern image editors can produce identity-preserving AIGC (IP-AIGC), where the same person appears with new attire, background, or lighting. The robustness and fairness of current detectors in this regime remain unclear, especially for under-represented populations. We present what we believe is the first systematic study of IP-AIGC detection for Indian and South-Asian faces, quantifying cross-generator generalization and intra-population performance. We assemble Indian-focused training splits from FairFD and HAV-DF, and construct two held-out IP-AIGC test sets (HIDF-img-ip-genai and HIDF-vid-ip-genai) using commercial web-UI generators (Gemini and ChatGPT) with identity-preserving prompts. We evaluate two state-of-the-art detectors (AIDE and Effort) under pretrained (PT) and fine-tuned (FT) regimes and report AUC, AP, EER, and accuracy. Fine-tuning yields strong in-domain gains (for example, Effort AUC 0.739 to 0.944 on HAV-DF-test; AIDE EER 0.484 to 0.259), but consistently degrades performance on held-out IP-AIGC for Indian cohorts (for example, AIDE AUC 0.923 to 0.563 on HIDF-img-ip-genai; Effort 0.740 to 0.533), which indicates overfitting to training-generator cues. On non-IP HIDF images, PT performance remains high, which suggests a specific brittleness to identity-preserving edits rather than a generic distribution shift. Our study establishes IP-AIGC-Indian as a challenging and practically relevant scenario and motivates representation-preserving adaptation and India-aware benchmark curation to close generalization gaps in AIGC detection.

