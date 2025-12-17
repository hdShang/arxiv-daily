---
layout: default
title: A Large Scale Benchmark for Test Time Adaptation Methods in Medical Image Segmentation
---

# A Large Scale Benchmark for Test Time Adaptation Methods in Medical Image Segmentation

**arXiv**: [2512.02497v1](https://arxiv.org/abs/2512.02497) | [PDF](https://arxiv.org/pdf/2512.02497.pdf)

**作者**: Wenjing Yu, Shuo Jiang, Yifei Chen, Shuo Chang, Yuanhan Wang, Beining Wu, Jie Dong, Mingxuan Liu, Shenghao Zhu, Feiwei Qin, Changmiao Wang, Qiyuan Tian

---

## 💡 一句话要点

**提出MedSeg-TTA基准以系统评估医学图像分割中的测试时适应方法**

**关键词**: `医学图像分割` `测试时适应` `域偏移` `基准评估` `多模态分析`

## 📋 核心要点

1. 核心问题：现有医学图像分割测试时适应评估在模态覆盖、任务多样性和方法一致性方面有限
2. 方法要点：统一评估20种代表性适应方法，涵盖七种成像模态和四种适应范式
3. 实验或效果：结果显示无单一范式在所有条件下最优，方法性能受模态和域偏移影响显著

## 📄 摘要（原文）

> Test time Adaptation is a promising approach for mitigating domain shift in medical image segmentation; however, current evaluations remain limited in terms of modality coverage, task diversity, and methodological consistency. We present MedSeg-TTA, a comprehensive benchmark that examines twenty representative adaptation methods across seven imaging modalities, including MRI, CT, ultrasound, pathology, dermoscopy, OCT, and chest X-ray, under fully unified data preprocessing, backbone configuration, and test time protocols. The benchmark encompasses four significant adaptation paradigms: Input-level Transformation, Feature-level Alignment, Output-level Regularization, and Prior Estimation, enabling the first systematic cross-modality comparison of their reliability and applicability. The results show that no single paradigm performs best in all conditions. Input-level methods are more stable under mild appearance shifts. Feature-level and Output-level methods offer greater advantages in boundary-related metrics, whereas prior-based methods exhibit strong modality dependence. Several methods degrade significantly under large inter-center and inter-device shifts, which highlights the importance of principled method selection for clinical deployment. MedSeg-TTA provides standardized datasets, validated implementations, and a public leaderboard, establishing a rigorous foundation for future research on robust, clinically reliable test-time adaptation. All source codes and open-source datasets are available at https://github.com/wenjing-gg/MedSeg-TTA.

