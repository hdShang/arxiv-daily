---
layout: default
title: Explainable Parkinsons Disease Gait Recognition Using Multimodal RGB-D Fusion and Large Language Models
---

# Explainable Parkinsons Disease Gait Recognition Using Multimodal RGB-D Fusion and Large Language Models

**arXiv**: [2512.04425v1](https://arxiv.org/abs/2512.04425) | [PDF](https://arxiv.org/pdf/2512.04425.pdf)

**作者**: Manar Alnaasan, Md Selim Sarowar, Sungho Kim

---

## 💡 一句话要点

**提出基于RGB-D多模态融合与大型语言模型的可解释帕金森病步态识别框架**

**关键词**: `帕金森病步态识别` `RGB-D多模态融合` `可解释人工智能` `大型语言模型` `时空特征提取`

## 📋 核心要点

1. 核心问题：现有帕金森病步态识别方法存在单模态输入、鲁棒性低和临床可解释性不足的局限。
2. 方法要点：采用双YOLOv11编码器提取RGB-D特征，结合多尺度局部-全局提取模块和跨空间融合机制增强时空表示。
3. 实验或效果：在多模态步态数据集上验证，该框架提高了识别准确率、环境鲁棒性，并通过冻结大型语言模型生成临床可解释文本。

## 📄 摘要（原文）

> Accurate and interpretable gait analysis plays a crucial role in the early detection of Parkinsons disease (PD),yet most existing approaches remain limited by single-modality inputs, low robustness, and a lack of clinical transparency. This paper presents an explainable multimodal framework that integrates RGB and Depth (RGB-D) data to recognize Parkinsonian gait patterns under realistic conditions. The proposed system employs dual YOLOv11-based encoders for modality-specific feature extraction, followed by a Multi-Scale Local-Global Extraction (MLGE) module and a Cross-Spatial Neck Fusion mechanism to enhance spatial-temporal representation. This design captures both fine-grained limb motion (e.g., reduced arm swing) and overall gait dynamics (e.g., short stride or turning difficulty), even in challenging scenarios such as low lighting or occlusion caused by clothing. To ensure interpretability, a frozen Large Language Model (LLM) is incorporated to translate fused visual embeddings and structured metadata into clinically meaningful textual explanations. Experimental evaluations on multimodal gait datasets demonstrate that the proposed RGB-D fusion framework achieves higher recognition accuracy, improved robustness to environmental variations, and clear visual-linguistic reasoning compared with single-input baselines. By combining multimodal feature learning with language-based interpretability, this study bridges the gap between visual recognition and clinical understanding, offering a novel vision-language paradigm for reliable and explainable Parkinsons disease gait analysis. Code:https://github.com/manaralnaasan/RGB-D_parkinson-LLM

