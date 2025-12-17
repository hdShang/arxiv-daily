---
layout: default
title: Toward Content-based Indexing and Retrieval of Head and Neck CT with Abscess Segmentation
---

# Toward Content-based Indexing and Retrieval of Head and Neck CT with Abscess Segmentation

**arXiv**: [2512.01589v1](https://arxiv.org/abs/2512.01589) | [PDF](https://arxiv.org/pdf/2512.01589.pdf)

**作者**: Thao Thi Phuong Dao, Tan-Cong Nguyen, Trong-Le Do, Truong Hoang Viet, Nguyen Chi Thanh, Huynh Nguyen Thuan, Do Vo Cong Nguyen, Minh-Khoi Pham, Mai-Khiem Tran, Viet-Tham Huynh, Trong-Thuan Nguyen, Trung-Nghia Le, Vo Thanh Toan, Tam V. Nguyen, Minh-Triet Tran, Thanh Dinh Le

---

## 💡 一句话要点

**提出AbscessHeNe数据集以支持头颈部脓肿分割及基于内容的CT检索研究。**

**关键词**: `头颈部脓肿分割` `CT影像数据集` `语义分割模型` `基于内容检索` `临床决策支持`

## 📋 核心要点

1. 核心问题：头颈部脓肿在CT影像中准确分割对临床诊断和治疗至关重要，但现有数据集和模型性能有限。
2. 方法要点：构建包含4,926张增强CT切片的数据集，提供像素级标注和临床元数据，评估CNN、Transformer和Mamba等分割模型。
3. 实验或效果：最佳模型Dice系数为0.39，IoU为0.27，表明任务挑战性大，需进一步研究提升性能。

## 📄 摘要（原文）

> Abscesses in the head and neck represent an acute infectious process that can potentially lead to sepsis or mortality if not diagnosed and managed promptly. Accurate detection and delineation of these lesions on imaging are essential for diagnosis, treatment planning, and surgical intervention. In this study, we introduce AbscessHeNe, a curated and comprehensively annotated dataset comprising 4,926 contrast-enhanced CT slices with clinically confirmed head and neck abscesses. The dataset is designed to facilitate the development of robust semantic segmentation models that can accurately delineate abscess boundaries and evaluate deep neck space involvement, thereby supporting informed clinical decision-making. To establish performance baselines, we evaluate several state-of-the-art segmentation architectures, including CNN, Transformer, and Mamba-based models. The highest-performing model achieved a Dice Similarity Coefficient of 0.39, Intersection-over-Union of 0.27, and Normalized Surface Distance of 0.67, indicating the challenges of this task and the need for further research. Beyond segmentation, AbscessHeNe is structured for future applications in content-based multimedia indexing and case-based retrieval. Each CT scan is linked with pixel-level annotations and clinical metadata, providing a foundation for building intelligent retrieval systems and supporting knowledge-driven clinical workflows. The dataset will be made publicly available at https://github.com/drthaodao3101/AbscessHeNe.git.

