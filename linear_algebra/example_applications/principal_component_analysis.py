import numpy as np
from pydantic import BaseModel
from typing import Dict, Tuple, Optional
from from_libs import Matrix, Vector

class VanillaPCA(BaseModel):
    pca_method: str = "traditional"

    def __init__(self, pca_method: str) -> None:
        pca_method = pca_method
    
    def _standardize_data(self, data: Matrix) -> Matrix:
        column_wise_mean = data.mean(axis=0)
        column_wise_std = data.std(axis=0)

        standardized_data = (data - column_wise_mean)/column_wise_std

        return standardized_data
    
    def _compute_covariance_matrix(self, standardized_data: Matrix) -> Matrix:
        covariance_matrix = np.cov(standardized_data, rowvar=False)

        return covariance_matrix
    
    def _compute_eigen_decomposition(self, covariance_matrix: Matrix) -> Dict[float, Vector]:
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
        eigen_values_vectors = {eigen_values[i]: eigen_vectors[:,i] for i in range(eigen_values.shape[0])}
        sorted_eigen_values_vectors = dict(sorted(eigen_values_vectors.items(), reverse=True))

        return sorted_eigen_values_vectors
    
    def _select_features(self, eigen_decomposition: Dict[float, Vector], n_feat_to_keep: int) -> Matrix:
        n_feat_to_keep = max(n_feat_to_keep, len(eigen_decomposition))
        eigen_items = list(eigen_decomposition.items())
        features = [eigen_items[i][1] for i in range(n_feat_to_keep)]

        features = np.vstack(features).T

        return features
    
    def _project_original_data(self, original_data: Matrix, feature_vector: Matrix) -> Matrix:
        projected_data = np.matmul(feature_vector.T, original_data.T).T

        return projected_data
    
    def compute_pca(self, data: Matrix, n_principal_components: int, project_data: bool=True) -> Tuple[Matrix, Optional[Matrix]]:
        # STEP 1: Standardize data
        standardized_data = self._standardize_data(data=data)
        # STEP 2: Computes covariance matrix
        cov_matrix = self._compute_covariance_matrix(standardized_data=standardized_data)
        # STEP 3: Compute eigen decomposition
        eigen_decomp_dict = self._compute_eigen_decomposition(covariance_matrix=cov_matrix)
        # STEP 4: Create feature vector
        feature_vector = self._select_features(eigen_decomposition=eigen_decomp_dict, n_feat_to_keep=n_principal_components)
        # STEP 5: Optional data projection
        projected_data = None
        if project_data:
            projected_data = self._project_original_data(original_data=standardized_data, feature_vector=feature_vector)
        
        return feature_vector, projected_data