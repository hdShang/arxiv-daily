---
layout: default
title: MF-GCN: A Multi-Frequency Graph Convolutional Network for Tri-Modal Depression Detection Using Eye-Tracking, Facial, and Acoustic Features
---

# MF-GCN: A Multi-Frequency Graph Convolutional Network for Tri-Modal Depression Detection Using Eye-Tracking, Facial, and Acoustic Features

**arXiv**: [2511.15675v1](https://arxiv.org/abs/2511.15675) | [PDF](https://arxiv.org/pdf/2511.15675.pdf)

**作者**: Sejuti Rahman, Swakshar Deb, MD. Sameer Iqbal Chowdhury, MD. Jubair Ahmed Sourov, Mohammad Shamsuddin

---

## 💡 一句话要点

**提出多频图卷积网络以解决基于眼动、面部和声音特征的抑郁症检测问题**

**关键词**: `多频图卷积网络` `抑郁症检测` `眼动特征` `面部特征` `声音特征` `多模态融合`

## 📋 核心要点

1. 现有图模型仅关注低频信息，限制了抑郁症检测的准确性
2. 引入多频滤波器模块，利用高低频信号增强特征提取
3. 在二元和三元分类任务中，模型敏感性和F2分数显著优于基线方法

## 📄 摘要（原文）

> Eye tracking data quantifies the attentional bias towards negative stimuli that is frequently observed in depressed groups. Audio and video data capture the affective flattening and psychomotor retardation characteristic of depression. Statistical validation confirmed their significant discriminative power in distinguishing depressed from non depressed groups. We address a critical limitation of existing graph-based models that focus on low-frequency information and propose a Multi-Frequency Graph Convolutional Network (MF-GCN). This framework consists of a novel Multi-Frequency Filter Bank Module (MFFBM), which can leverage both low and high frequency signals. Extensive evaluation against traditional machine learning algorithms and deep learning frameworks demonstrates that MF-GCN consistently outperforms baselines. In binary (depressed and non depressed) classification, the model achieved a sensitivity of 0.96 and F2 score of 0.94. For the 3 class (no depression, mild to moderate depression and severe depression) classification task, the proposed method achieved a sensitivity of 0.79 and specificity of 0.87 and siginificantly suprassed other models. To validate generalizability, the model was also evaluated on the Chinese Multimodal Depression Corpus (CMDC) dataset and achieved a sensitivity of 0.95 and F2 score of 0.96. These results confirm that our trimodal, multi frequency framework effectively captures cross modal interaction for accurate depression detection.

